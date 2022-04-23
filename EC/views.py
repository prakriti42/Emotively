<<<<<<< HEAD

from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import views
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


=======
from django.shortcuts import render
from . import views
import pickle
from pydub import AudioSegment
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a
# Create your views here.
def app(request):
    return render(request, 'app.html')

<<<<<<< HEAD

def getduration(audio):
    duration = audio.duration_seconds
    return duration

def saveAudio(request):
    if request.method == 'POST':
        audioData = request.POST['player']
        duration = getduration(audioData)
        Audio_Storage(user=request.user, recording=audioData , duration=duration).save()
        return HttpResponseRedirect("/")
    
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

def getPrediction(request,audio):   
    if request.method == 'POST':
        audio= request.POST['audio']  
        print(type(audio))  
        file_name = "/home/prakriti/College/FYP/Project/Emotively/sound.wav"
        audio11 = AudioSegment.from_file(audio , format="wav")
        model = pickle.load(open('speechemotionclassifier' , 'rb'))
        stereo_audio = AudioSegment.from_file(audio,format="wav")
        mono_audios = stereo_audio.split_to_mono()
        mono_left = mono_audios[0].export("predictemotion.wav",format="wav")
        soundfile = "predictemotion.wav"
        feature = extract_feature(soundfile, mfcc=True, chroma=True, mel=True)
        xpred = np.array(feature.reshape(1, -1))
        res = model.predict(xpred)
        result = f"You sound {res[0]}"
        print("Detected Emotion")
        return render(request, "app.html", {'result': result})

def result(request):
    audioData = request.GET['input-audio']

def log(request):
    audioData = Audio_Storage.objects.filter(user=request.user)
    users = len(Profile.objects.all())
    count = len(audioData)
    context = {'audio' : audioData , 'totalAudio' : count , 'users' : users}
    return render(request, 'log.html' ,context)


=======
def getPrediction(audio):
    model = pickle.load(open('speechemotionclassifier' , 'rb'))

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
    
    stereo_audio = AudioSegment.from_file(audio,format="wav")
    mono_audios = stereo_audio.split_to_mono()
    mono_left = mono_audios[0].export("predictemotion.wav",format="wav")
    soundfile = "predictemotion.wav"
    feature = extract_feature(soundfile, mfcc=True, chroma=True, mel=True)
    xpred = np.array(feature.reshape(1, -1))
    res = myClassifier.predict(xpred)

    return res 

def result(request):
    audioData = request.GET['input-audio']
def log(request):
    return render(request, 'log.html')
>>>>>>> 9735a40054aea9923a99f1ba17fcb6bd82531b7a



    