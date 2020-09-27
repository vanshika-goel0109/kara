from datetime import datetime
from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb
import os
import time


language = 'en'
r2 = sr.Recognizer()


def getData():

    with sr.Microphone() as source:  # stores the purpose
        print("speak")
        r2.adjust_for_ambient_noise(source, duration=20)
        purpose = r2.listen(source)
        start_time = time.time()
        print(r2.recognize_google(purpose))
        print("--- %s seconds ---" % (time.time() - start_time))
