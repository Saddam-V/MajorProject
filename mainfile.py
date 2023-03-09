from multiprocessing import Process
from comm import key_det, listen, speak, lislim
from y_download import p_fun, y_fun, i_fun
from b_soup import googlefun, open_brows
import pyperclip as pc
import pywhatkit as kt
import pyttsx3

while True:
    if(key_det('jarvis') == 1):
        query = listen()
        query = query.lower()

        if('open' in query):
            open_brows(query)
        elif(('youtube' in query)):
            y_fun(query)
        elif('download' in query):
            if('image' in query):
                pst = pc.paste()
                i_fun(pst, query)
            elif('pdf' in query):
                pst = pc.paste()
                p_fun(pst)
        elif 'search for' in query:
            query = query.replace("search for", " ", 10)
            kt.search(query)
        else:
            speak(googlefun(query))
