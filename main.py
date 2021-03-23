import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import webbrowser

r=sr.Recognizer()

askname=["what",'is','name','your']

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)#stores the audio file from microphone
        voice_data=""
        try:
            voice_data=r.recognize_google(audio)#creates it into data
        except sr.UnknownValueError:
            speak("Can't Undertsand, what you saying.")
        except sr.RequestError:
            speak("Sorry, Google Service is feeling lazy.")
        return voice_data

def respond(voice_data):
    if askname[0] and askname[1] and askname[2] and askname[3] in voice_data:
        speak("I'm Chip.")
    if 'What time is it'.lower() or 'what is the time'.lower() in voice_data:
        speak(ctime())
    if 'Search'.lower() in voice_data:
        search=record_audio("What you want to search for?")
        url='https://google.com/search?q='+search
        webbrowser.get('windows-default').open(url)
        speak('Here is what I found for '+ search)
    if 'Find location'.lower() in voice_data:
        location=record_audio("What's the location?")
        url='https://google.nl/maps/place/' +location +'/&amp;'
        webbrowser.get('windows-default').open(url)
        speak('Found the location of '+ location)
    if 'Exit'.lower() in voice_data:
        speak('Bye Bye.')
        exit()

def speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,100000000000)
    audio_file=f'audio-{str(r)}.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

#continuous listening
time.sleep(1)
speak("How can I help you ?")
while 1:
    voice_data=record_audio()
    respond(voice_data.lower())