import pyaudio
import keyboard
import time
import wave

chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100
Output_Filename = "Recorded.wav"
p = pyaudio.PyAudio() 

stream = p.open(format=format,  
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

frames = []
print("Press SPACE to start recording")
keyboard.wait('space')
print("Recording... Press SPACE to stop.")
time.sleep(0.2)

while True:
    try:
        data = stream.read(chunk)
        frames.append(data)
    except KeyboardInterrupt:
        break
    if keyboard.is_pressed('space'):
        print("stopping recording")
        time.sleep(0.2)
        break  

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(Output_Filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()