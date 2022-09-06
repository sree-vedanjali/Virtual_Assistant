import pyttsx3 #(text to speech)
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[1].id)
    if voice == 1:   
        engine.setProperty('voice', voices[0].id)
    
    if voice == 2:
        engine.setProperty('voice', voices[1].id)

    speak("hello, i'm your assistant")   

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    elif hour >= 16 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night")

def wishme():
    speak("Welcome back")
    time()
    date()
    greeting()
    speak("How can i help u?")
    
'''while True:
    voice = int(input("]press 1 for male voice\n2 for female voice\n"))
    #speak(audio)
    getvoices(voice)'''
#time()
#date()
wishme()
    
