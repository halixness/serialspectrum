import pyaudio
import numpy as np
import serial
import time
import wave
from threading import Thread
from tkinter import *

port = 'COM4'
songPath = 'thesong.wav'
pause = True



# Play/Pause Switch Method
def playpause():

    global pause

    if pause:
        pause = False
    else:
        pause = True





# Threaded Player
def threaded_function():

    global pause
    global songPath
    global data
    
    chunk = 1024
    
    wf = wave.open(songPath, 'rb')
    p=pyaudio.PyAudio()
    
    # Open Stream
    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)

    while data != '':

        while pause:
            pass
        
        stream.write(data)
        data = wf.readframes(chunk)
        global_data = data



# GUI
window = Tk()
window.title("Music Player")
songLabel = StringVar()

Label(window, textvariable=songLabel).pack()

Label(window, text="Simple VU Meter", font=("Helvetica", 30)).pack()

Label(window, text="Selected song : " + songPath + "\n", font=("Helvetica", 10)).pack()

Button(window, text="Play/Pause", command=playpause).pack()

Label(window, text="\n").pack()


# Settings
chunk = 1024
RATE = 44100
ser = serial.Serial(port, 9600)

wf = wave.open(songPath, 'rb')
data = wf.readframes(chunk)

# Player
thread = Thread(target = threaded_function, args = ())
thread.start()

while data != '':

    window.mainloop()

    while pause:
        pass

    # Analyzer Instructions
    
    data2 = np.fromstring(data,dtype=np.int16)

    peak=np.average(np.abs(data2))*2

    bar_n = int(50*peak/2**16)

    # Visualizer
    bars="#"*bar_n
    print(bars)

    # Serial Communications
    ser.write(str(bar_n).encode())
    

thread.stop()
ser.close()
stream.close()
p.terminate()
