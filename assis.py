import speech_recognition as sr
import webbrowser as wb

r2 = sr.Recognizer()

#inputs for meeting reminder
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source, duration=5)
    print('tell me the event please')
    audio = r2.listen(source)
    print(r2.recognize_google(audio))

def func():
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source, duration=5)
        print('tell me date')
        audio = r2.listen(source)
        print(r2.recognize_google(audio))

func()
