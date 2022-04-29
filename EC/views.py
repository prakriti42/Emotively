
from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from django.contrib import messages
import pickle
from pydub import AudioSegment
from .models import Audio_Storage 
from UMS.models import Profile 
import pandas as pd
import pickle 
import librosa
import soundfile as sf
import os, glob, pickle
import numpy as np
from datetime import datetime
from django.core.files.storage import FileSystemStorage


# Create your views here.
def app(request):
    return render(request, 'app.html')


def getduration(audio):
    duration = audio.duration_seconds
    return duration

def saveAudio(request):
    audioData = None 
    if request.method == 'POST':
        try : 
            audioData = request.FILES['audio']
        except :
            print("No Audio stored")
        if audioData is not None:
            audio = request.FILES['audio']
            fs = FileSystemStorage()
            filename = fs.save(audio.name, audio)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)
            Audio_Storage(audio_file= uploaded_file_url , user=request.user ,  dateofUpload=datetime.now()).save()
        # duration = 10
        # Audio_Storage(user=request.user, audio_file= audioData, recordingname= request.user , duration=duration, dateofUpload=datetime.now()).save()
            messages.success(request, 'Audio Saved Successfully')
        return redirect(app)
    
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
            return result

def getPrediction(request): 
    audioData = None  
    if request.method == 'POST':
            audio = request.FILES['audio']
            fs = FileSystemStorage()
            filename = fs.save(audio.name, audio)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url) 
            model = pickle.load(open('speechemotionclassifier' , 'rb'))
            stereo_audio = AudioSegment.from_file(uploaded_file_url,format="wav")
            mono_audios = stereo_audio.split_to_mono()
            mono_left = mono_audios[0].export("predictemotion.wav",format="wav")
            soundfile = "predictemotion.wav"
            feature = extract_feature(soundfile, mfcc=True, chroma=True, mel=True)
            xpred = np.array(feature.reshape(1, -1))
            res = model.predict(xpred)
            result = res[0]
            print(result)
            print("Detected Emotion")
            return render(request, "app.html", {'result': result})
    else:
            print("No Audio Detected")
            return render(request, "app.html", {'result': "Anger"})

def result(request):
    audioData = request.GET['input-audio']

def log(request):
    audioData = Audio_Storage.objects.filter(user=request.user)
    users = len(Profile.objects.all())
    td = Profile.objects.values_list('totalDetection' , flat= True)
    detection_count = sum(list(td))
    count = len(audioData)
    context = {'audio' : audioData , 'totalAudio' : count , 'users' : users , 'detection_count' : detection_count}
    return render(request, 'log.html' ,context)





    