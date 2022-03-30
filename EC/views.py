from django.shortcuts import render
from . import views
import pickle
from pydub import AudioSegment
# Create your views here.
def app(request):
    return render(request, 'app.html')

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



    