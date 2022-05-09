
from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from django.contrib import messages
import pickle
from pydub import AudioSegment
from .models import Audio_Storage 
from UMS.models import Profile 
from IPython.display import Audio
import pandas as pd
import pickle 
import librosa
import soundfile as sf
import os, glob, pickle
import numpy as np
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import base64
import json
import requests
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import urllib.request 
import wave

# Create your views here.
@login_required
def app(request):
    return render(request, 'app.html')


val = 0


def getduration(audio):
    duration = audio.duration_seconds
    return duration

def saveAudio(request):
    
    data_str = request.body.decode('ascii')
    data = json.loads(data_str)
    audio = data['audio']
    wav_file = open("recent.wav", "wb")
    decode_string = base64.b64decode(audio)
    wav_file.write(decode_string)
    x,_ = librosa.load('recent.wav', sr=16000)
    sf.write('tmp.wav', x, 16000)
    global val
    val = 1
    print("Flag at saveAudio is" , val)
    return redirect(to='/app')


def savetoModel(request):
    if request.method == 'POST':
                        audioData = request.FILES['audiofile']
                        fs = FileSystemStorage()
                        filename = fs.save(audioData.name, audioData)
                        uploaded_file_url = fs.url(filename)
                        print(request.FILES.get('data'))
                        print("The file url is :"+uploaded_file_url) 
                        td = Profile.objects.values_list('totalDetection' , flat= True)
                        Audio_Storage(audio=request.FILES['audiofile'], recordingname=request.user, user=request.user , dateofUpload= datetime()).save()

                        print(td)
                        return render(request, "app.html")
    else :
        Audio_Storage(audio=request.FILES['audiofile'], recordingname=request.user, user=request.user , dateofUpload= datetime()).save()

def extract_feature(file_name, mfcc, chroma, mel):
            with sf.SoundFile(file_name) as sound_file:
                X = sound_file.read(dtype="float32")
                sample_rate=sound_file.samplerate
                if chroma:
                    stft=np.abs(librosa.stft(X))
                result=np.array([])
                if mfcc:
                    mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
                    result=np.hstack((result, mfccs))
                if chroma:
                    chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
                    result=np.hstack((result, chroma))
                if mel:
                    mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
                    result=np.hstack((result, mel))
                # mean_mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=49).T,axis=0) 
                # std_mfccs = np.std(librosa.feature.mfcc(y=x, sr=sr, n_mfcc=number_of_mfcc_features).T,axis=0)
            return result



def getPrediction(request): 
    try:
            model = pickle.load(open('speechemotionclassifier' , 'rb'))
            global val
            flag = val 
            print("Flag at getPrediction is" , flag)
            print("The Value of flag is" , str(val))
            print("Flag at line 77 is" , flag)
            if flag == 0 : 
                if request.method == 'POST':
                    audioData = request.FILES['audiofile']
                    fs = FileSystemStorage()
                    filename = fs.save(audioData.name, audioData)
                    uploaded_file_url = fs.url(filename)
                    print(request.FILES.get('data'))
                    print("The file url is :"+uploaded_file_url) 
                    feature = extract_feature("tmp.wav", mfcc=True, chroma=True, mel=True)
                    xpred = np.array(feature.reshape(1, -1))
                    res = model.predict(xpred)
                    result = res[0]
                    print(result)
                    # val = 1
                    print("Detected Emotion fopm file upload")
                    td = Profile.objects.get(user=request.user).totalDetection
                    Profile.objects.filter(pk=request.user).update(totalDetection=td+1)
                    print("Updated total detection" , td)
                    Audio_Storage(audio_file=request.FILES['audiofile'], recordingname=request.user, user=request.user , Tag = result, dateofUpload= datetime.now()).save()
                    print("Audio Storage save done")
                    return render(request, "app.html", {'result': result})
            else :
                feature = extract_feature("tmp.wav", mfcc=True, chroma=True, mel=True)
                print(feature)
                xpred = np.array(feature.reshape(1, -1))
                print(xpred)
                res = model.predict(xpred)
                result = res[0]
                print(result)
                print("Detected Emotion")
                print("Detected Emotion frpm file recording")
                # flag = 0
                val = 0
                print("Flag has been set to" , str(val))
                td = Profile.objects.get(user=request.user).totalDetection
                Profile.objects.filter(pk=request.user).update(totalDetection=td+1)
                recordingname=str(request.user)+"_"+str(td+1)
                Audio_Storage(audio_file="tmp.wav", recordingname=recordingname, user=request.user, Tag = result, dateofUpload= datetime.now()).save()
                print("Audio Storage save done")
                print("Updated total detection" , td)
                return render(request, "app.html", {'result': result})
      
    except Exception as e:
        print("Error is " , e)
        return render(request, "app.html", {'result': "Error Encountered : Did you submit the audio sample?"})


@login_required
def log(request):
    audioData = Audio_Storage.objects.filter(user=request.user)
    users = len(Profile.objects.all())
    td = Profile.objects.values_list('totalDetection' , flat= True)
    detection_count = sum(list(td))
    count = len(audioData)
    context = {'audio' : audioData , 'totalAudio' : count , 'users' : users , 'detection_count' : detection_count}
    return render(request, 'log.html' ,context)





    