import speech_recognition as sr
from ui import MyApp

r = sr.Recognizer()

def talk_and_recognize():
    '''
    function to take the text from speech
    return query -> the text version of the speech to be recognised
    '''
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 0.7
        r.energy_threshold = 1400
        audio = r.listen(source)
        print('Recognizing....')
        query = r.recognize_google(audio,language='en-in')
    
    return query

q = talk_and_recognize()
app = MyApp()
WIDGETS = ['button','text input','label']           # currenty supporting widgets for the GUI


## checking for the widget to draw
wid = False
for i in WIDGETS:
    if i in q:
        wid = i
        break

if wid:
    app.make('button')
else:
    app.make('text',q)

app.run()