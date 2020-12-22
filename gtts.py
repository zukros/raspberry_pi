""".
dependencies:

pip3 install gTTs

"""

from gtts import gTTS
import pygame as py


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    py.mixer.init()
    py.mixer.music.load(filename)
    py.mixer.music.play()
    
    
speak('Hello, How are you')




