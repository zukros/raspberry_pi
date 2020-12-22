""".
pip3 install numpy
pip3 install gTTs

Descption:


"""

import RPi.GPIO as GPIO
from time import sleep
import time
import numpy as np
from gtts import gTTS
import pygame as py
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    py.mixer.init()
    py.mixer.music.load(filename)
    py.mixer.music.play()


try:
    while 1:
        
        for i in np.arange(11, 0, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(1)
            num = str(int(i)) 
            print("ClockWise: ", i)
            speak(num)
         
        for i in np.arange(1, 11, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(1)
            num = str(int(i))            
            print("AntiClockwise: ", num)
            speak(str(int(i)))
            
                 
except KeyboardInterrupt: 
     pass


pwm.stop()
GPIO.cleanup()
print ("Done")
