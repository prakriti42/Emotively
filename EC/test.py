import librosa
import wave
import soundfile as sf
x,_ = librosa.load('recent.wav', sr=16000)
sf.write('tmp.wav', x, 16000)
wave.open('tmp.wav','r')

