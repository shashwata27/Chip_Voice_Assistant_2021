import speech_recognition as sr
from time import ctime
import time
import webbrowser

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)#stores the audio file from microphone
        voice_data=""
        try:
            voice_data=r.recognize_google(audio)#creates it into data
        except sr.UnknownValueError:
            print("Can't Undertsand, what you saying.")
        except sr.RequestError:
            print("Sorry, Google Service is feeling lazy.")
        return voice_data

def respond(voice_data):
    if "What your name".lower() in voice_data:
        print("I'm Chip.")
    if 'What time is it'.lower() in voice_data:
        print(ctime())
    if 'Search'.lower() in voice_data:
        search=record_audio("What you want to search for?")
        url='https://google.com/search?q='+search
        webbrowser.get('windows-default').open(url)
        print('Here is what I found for '+ search)
    if 'Find location'.lower() in voice_data:
        location=record_audio("What's the location?")
        url='https://google.nl/maps/place/' +location +'/&amp;'
        webbrowser.get('windows-default').open(url)
        print('Found the location of '+ location)
    if 'Exit'.lower() in voice_data:
        print('Bye Bye.')
        exit()

#continuous listening
time.sleep(1)
print("How can I help you ?")
while 1:
    voice_data=record_audio()
    respond(voice_data.lower())