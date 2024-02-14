import pyaudio
import wave
import keyboard
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1    
RATE = 44100    
CHUNK = 1024
OUTPUT_FILENAME =   "recordedFile.wav"

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

frames = []
print("Press SPACE to start recording.")
keyboard.wait('space')
print("Recording... Press Space to stop.")
time.sleep(0.2)

while True:
    try:
        data = stream.read(CHUNK)
        frames.append(data)
    except KeyboardInterrupt:
        break
    if keyboard.is_pressed('space'): # Save the recording and exit
        print("\n\nStopping Recording after a brief delay ... ")
        time.sleep(0.2)
        break       


stream.stop_stream()
stream.close()
audio.terminate()


waveFile = wave.open(OUTPUT_FILENAME, 'wb')
# set the parameters of the WAVE file (sample rate, sample width, etc.)
waveFile.setnchannels(CHANNELS)           # mono
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)               # sample rate
# write frames of data to the WAVE file
waveFile.writeframe(b''.join(frames))      # write frames of data to file
# close the file
waveFile.close()                          # Close the file when done
print("Finished!")
