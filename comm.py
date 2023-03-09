from multiprocessing import Process
import keyboard
from logging import exception
import speech_recognition as sr
import pyttsx3
import winsound
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import os
import multiprocessing
import pyaudio


############################################################################
r = sr.Recognizer()

##############################
modeldir = "files/sphinx/models"
config = Decoder.default_config()

config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-dict', os.path.join(modeldir,
                                        'en-us/cmudict-en-us.dict'))
# disable -logfn to get logs in console

#decoder = Decoder(config)
##############################
engine = pyttsx3.init()

# change the speech rate
engine.setProperty('rate', 160)

# get the available voices
voices = engine.getProperty('voices')

# choose a voice based on the voice id
engine.setProperty('voice', voices[0].id)
# Selected Brian Voice
####################################################################


# FOR SPEAKING
# ---------------
def speak(query):
    engine.say(query)
    engine.runAndWait()
# ---------------


def listen():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2)
            duration = 70  # milliseconds
            freq = 360  # Hz
            winsound.Beep(freq, duration)
            audio2 = r.listen(source2)
            print("recognizing")
            MyText = r.recognize_google(audio2, language='en')
            print('did you say '+MyText)

            return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "No"
    except sr.UnknownValueError:
        print(". . .")
        return "No"


# TO LISTEN FOR LIMITED TIME
# ----------------------------
def lislim(n):
    try:
        with sr.Microphone() as source2:
            r.pause_threshold = 0.7
            r.energy_threshold = 6000
            duration = 70  # milliseconds
            freq = 360  # Hz
            audio2 = r.record(source2, duration=n)
            winsound.Beep(freq, duration)
            print("a")
            MyText = r.recognize_google(audio2, language='en')

        MyText = MyText.lower()
        print("Did you say " + MyText)
        return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return 'NO'
    except sr.UnknownValueError:
        print(". . .")
        return 'NO'


# FOR DETECTING KEYWORD
# ------------------------
def key_det(str):
    config.set_string('-logfn', 'files/sphinx.log')
    config.set_string('-keyphrase', str)
    p = pyaudio.PyAudio()
    #decoder.set_kws('keyword', 'keyword.list')
    # decoder.set_search('keyword')

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
            print("Detected keyword")

            decoder.end_utt()
            return 1
            # decoder.start_utt()
