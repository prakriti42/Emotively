import pandas as pd
import pickle 
import librosa
import soundfile as sf
import os, glob, pickle
import numpy as np

myClassifier = pickle.load(open('speechemotionclassifier' , 'rb'))


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


# Python3 program to illustrate
# splitting stereo audio to mono
# using pydub

# Import AudioSegment from pydub
from pydub import AudioSegment

# Open the stereo audio file as
# an AudioSegment instance
stereo_audio = AudioSegment.from_file("file.wav",format="wav")

# Calling the split_to_mono method
# on the stereo audio file
mono_audios = stereo_audio.split_to_mono()
 
# Exporting/Saving the two mono
# audio files present at index 0(left)
# and index 1(right) of list returned
# by split_to_mono method
mono_left = mono_audios[0].export("predictemotion.wav",format="wav")

# soundfile = "NewDataset/Sad/sa2.wav"
soundfile = "predictemotion.wav"
feature = extract_feature(soundfile, mfcc=True, chroma=True, mel=True)
xpred = np.array(feature.reshape(1, -1))

res = myClassifier.predict(xpred)

print(f"Predicted the emotion as {str(res)}")

