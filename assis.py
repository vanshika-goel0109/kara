import speech_recognition as sr
import webbrowser as wb

r2 = sr.Recognizer()

with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source, duration=5)
    print('speak now...')
    audio = r2.listen(source)
    print(r2.recognize_google(audio))

def func():
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source, duration=5)
        print('search your query')
        audio = r2.listen(source)

    get = r2.recognize_google(audio)
    print(get)
