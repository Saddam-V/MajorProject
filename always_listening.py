import sys
import os
import pyaudio
import winsound
import pywhatkit as kt
# Import required modules
import pyautogui
import time
import speech_recognition as sr
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from gtts import gTTS
from time import sleep
import os
import pyglet
import wikipedia
import webbrowser
import wolframalpha
# import temp as tmp
import pyttsx3
import random
import winsound
# Import required modules
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import keyboard
import sys
import pyperclip as pc
from tkinter import messagebox
import subprocess as sp
import howdoi
import apiclient
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
import datefinder
from tensorflow import *

r = sr.Recognizer()
modeldir = "files/sphinx/models"
###################################################### my Fun #####################################################
credentials = pickle.load(open("token.pkl", "rb"))
# #######################Google calender#####################
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", scopes=scopes)

service = apiclient.discovery.build(
    "calendar", "v3", credentials=credentials, static_discovery=False)
# ########################pyttsx3###########################################
# ##########################wolform alpha#########################
app_id = '5R5YX2-U9JQ68K8A7'

client = wolframalpha.Client(app_id)
############################################################################
engine = pyttsx3.init()

# change the speech rate
engine.setProperty('rate', 165)

# get the available voices
voices = engine.getProperty('voices')

# choose a voice based on the voice id
engine.setProperty('voice', voices[0].id)
# Selected Brian Voice
####################################################################

credentials = pickle.load(open("token.pkl", "rb"))
temp = 0


def googlefun(text):
    URL = "https://www.google.co.in/search?q=" + text

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        result = soup.find(class_='Z0LcW CfV8xf').get_text()
        print(result)
        return result
    except:
        try:
            result = soup.find(
                class_='hgKElc').get_text()
            print('def')
            print(result)
            return result
        except:
            try:
                result = soup.find(
                    class_='YOGjf').get_text()
                print('abc')
                return result
            except:
                result = soup.find(
                    class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                print('abc')
                return result


def SpeakText(text):
    if (text == "p"):
        # mytext = "Ready for command sir!"
        kt.info("Python")
        # y = random.choice(list1)
        # x = tmp.emotion()
        # print(x)
        # if(x == "happy"):

        #     mytext = "Good to see you happy!" + \
        #         content[y] + "How can I help you?"
        # elif(x == "sad"):
        #     mytext = "You look sad,"+content[y] + " Can I help you in any way?"
        # elif(x == "neutral"):
        #     mytext = "Too neutral."+content[y] + " How can I help?"
        # elif(x == "excited"):
        #     mytext = "Wow! you are so excited!"+content[y]
    elif 'open youtube' in text:
        webbrowser.open_new_tab("https://www.youtube.com")
        mytext = "Here it is!"

    elif 'open google' in text:
        webbrowser.open_new_tab("https://www.google.com")
        mytext = "There you go! Google is here"

    elif 'open gmail' in text:
        webbrowser.open_new_tab("gmail.com")
        mytext = "Google Mail open now"

    elif 'search for' in text:
        text = text.replace("search for", " ", 10)
        kt.search(text)
        mytext = "Here it is..."

    elif ('on youtube' in text):
        text = text.replace("on youtube", " ", 10)
        kt.playonyt(text)
        mytext = "Your" + text + " here sir"

    elif ('notes' in text) or ('open writingpad' in text) or ('open note' in text):
        webbrowser.open_new_tab("https://notepad.pw/saddamnotestemp")
        mytext = "Sir,"
        # os.system("Notepad")
        # mytext = "Yes sir!"
    elif ("open vlc" in text) or ("player" in text) or ("video player" in text) or ("vlc" in text):
        os.system("VLC Media Player")
        mytext = "VLC here"

    elif ('how do i' in text):
        text = text.replace("how do i ", "", 9)
        print(text)
        # msg = os.system('howdoi '+text)
        try:
            output = sp.getoutput('howdoi '+text+' -n 4')
            mytext = googlefun(text)
        except:
            try:
                output = sp.getoutput('howdoi '+text)
                mytext = " "
                # mytext = googlefun(text)
            except:
                # mytext = googlefun(text)
                mytext = " "
                print('abc')

        messagebox.showinfo("Answer", output)

    # elif (('add to calendar' in text) or ('add to my calendar' in text)):
    #     text1 = text.replace("add to calender", "", 15)
    #     print(text1)
    #     try:
    #         created_event = service.events().quickAdd(
    #             calendarId='primary',
    #             text=text1).execute()

    #         print(created_event['id'])
    #         mytext = "Event created successfully"
    #     except:
    #         mytext = "Sorry sir, some error occured"

    elif (('calendar today' in text) or ('events today' in text)):
        try:
            today = datetime.today()
            start = (datetime(today.year, today.month,
                     today.day, 00, 00)).isoformat() + 'Z'
            tomorrow = today + timedelta(days=1)
            end = (datetime(tomorrow.year, tomorrow.month,
                   tomorrow.day, 00, 00)).isoformat() + 'Z'
            print('Getting todays events')
            events_results = service.events().list(calendarId='primary', timeMin=start,
                                                   timeMax=end, singleEvents=True, orderBy='startTime').execute()
            mytext = "Your events today are, " + \
                events_results['items'][0]['summary']
        except:
            mytext = 'no events found'

    elif 'keep my pc awake' in text:
        mytext = 'on it sir,'
        pyautogui.FAILSAFE = False
        while True:
            time.sleep(15)
            for i in range(0, 100):
                pyautogui.moveTo(0, i * 5)
            for i in range(0, 3):
                pyautogui.press('shift')

    elif 'copy' in text:
        name = 'Mahammad Shafin Vohra'
        email = 'mohammedshafin055@gmail.com'
        number = '7487812395'
        if('name' in text):
            pc.copy(name)
        elif('mail' in text):
            pc.copy(email)
        elif('number' in text):
            pc.copy(number)
        elif('info' in text):
            pc.copy(name)
            pc.copy(email)
            pc.copy(number)

        mytext = "copied"

    elif 'shutdown now' in text:
        return os.system("shutdown /s /t 1")
    elif 'reboot now' in text:
        return os.system('shutdown /r /t 1')
    else:
        try:
            try:
                res = client.query(text)
                mytext = next(res.results).text
            except:

                mytext = googlefun(text)

            # print("kindly wait while i search wikipedia")
            # mytext = wikipedia.summary(text, sentences=2)
        except:
            mytext = "Sorry! Result not found"
    # init function to get an engine instance for the speech synthesis
    # say method on the engine that passing input text to be spoken
    engine.say(mytext)
    engine.runAndWait()
    global y
    # y = time.time()
    # language = 'en'

    # myobj = gTTS(text=mytext, lang=language, slow=False)
    # filename = "temp.mp3"
    # myobj.save(filename)

    # music = pyglet.media.load(filename, streaming=False)
    # music.play()

    # sleep(music.duration)
    # os.remove(filename)
###################################################### my Fun #####################################################


# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
# disable -logfn to get logs in console
config.set_string('-logfn', 'files/sphinx.log')
config.set_string('-keyphrase', 'jarvis')
#decoder = Decoder(config)

#decoder.set_kws('keyword', 'keyword.list')
# decoder.set_search('keyword')

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024)

    decoder.process_raw(buf, False, False)

    if decoder.hyp() != None:
        print([(seg.word, seg.prob, seg.start_frame, seg.end_frame)
              for seg in decoder.seg()])
        for seg in decoder.seg():
            print(seg.word)
            break
        print("Detected keyword, restarting search")
        #
        # Here you run the code you want based on keyword
        try:
            with sr.Microphone() as source2:
                # r.pause_threshold = 0.7
                # r.energy_threshold = 6000
                r.adjust_for_ambient_noise(source2)
                # print("Listening...")
                duration = 70  # milliseconds
                freq = 360  # Hz
                # ###################################
                # x = time.time()
                # #################################
                # audio2 = r.record(source2, duration=3)
                winsound.Beep(freq, duration)
                # engine.say('sir')
                # engine.runAndWait()
                audio2 = r.listen(source2)
                print("a")
                # print("Recognizing...")
                MyText = r.recognize_google(audio2, language='en')

            MyText = MyText.lower()
            print("Did you say " + MyText)
            SpeakText(MyText)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print(". . .")
        #
        decoder.end_utt()
        decoder.start_utt()
