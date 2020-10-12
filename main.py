import speech_recognition as sr
from ui import MyApp

r = sr.Recognizer()

def talk_and_recognize():
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 0.7
        r.energy_threshold = 1400
        audio = r.listen(source)
        print('Recognizing....')
        query = r.recognize_google(audio,language='en-in')
        # print(f'User said: {query}')
    
    return query

q = talk_and_recognize()
app = MyApp()
app.showText(q)
app.run()