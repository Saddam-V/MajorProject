# importing the module
from random import Random
from pytube import YouTube
from pytube import Search
from pytube import Channel
import pyperclip as pc
import urllib.request
import requests
from PIL import Image
from comm import speak, listen, key_det
import pywhatkit as kt
from icrawler.builtin import GoogleImageCrawler


SAVE_PATH = "C:/Users/shafin/Desktop/"


# DOWNLOAD YOUTUBE VIDEO
# -------------------------
def y_fun(query):
    speak('sir')
    # try:

    if 'link' in query:
        pst = pc.paste()
        link = YouTube(pst)

    elif 'play' in query:
        query = query.replace("on youtube", " ", 10)
        kt.playonyt(query)
        return 1

    elif 'search' in query:
        text = query.replace("search for ", " ", 11)
        text = text.replace(" on youtube", " ", 11)
        s = Search(text)
        try:
            vid = s.results
        except:
            speak('Please connect.')
            return 0
        leng = 0
        temp = ""
        while(temp != 'yes' or leng <= len(vid)):
            c_url = vid[leng].channel_url
            c = Channel(c_url)
            speak(vid[leng].title + 'from' + c.channel_name)
            temp = listen()
            if(('download' in temp) or ('yes' in temp)):
                link = vid[leng]
                temp = 'yes'
                break
            elif('show' in temp):
                urllib.request.urlretrieve(
                    vid[leng].thumbnail_url,
                    "gfg.png")
                img = Image.open("gfg.png")
                img.show()
            elif('play' in temp):
                kt.playonyt(vid[leng].title)
                return 1
            else:
                leng = leng+1
                key_det('next')
        print(text)
    else:
        text = query.replace("download ", " ", 9)
        text = text.replace(" from youtube", " ", 13)
        s = Search(text)
        try:
            vid = s.results
        except:
            speak('Please connect.')
            return 0
        link = vid[0]

    link.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(SAVE_PATH)


# DOWNLOAD IMAGE
# -------------------
def i_fun(link, query):
    if('link' in query):
        urllib.request.urlretrieve(
            link,
            "C:/Users/shafin/Desktop/S_Assistant/gfg.png")
        img = Image.open("C:/Users/shafin/Desktop/S_Assistant/gfg.png")
        img.show()
    else:
        try:
            temp = query.split("image of ", 1)[1]
        except:
            temp = query.split("images of", 1)[1]
        google_Crawler = GoogleImageCrawler(
            storage={'root_dir': r'C:/Users/shafin/Desktop/S_Assistant/'})
        google_Crawler.crawl(keyword=temp, max_num=10)
    speak('downloaded')

# DOWNLOAD PDF
# ---------------------


def p_fun(link):
    r = requests.get(link, stream=True)
    with open("C:/Users/shafin/Desktop/S_Assistant/python.pdf", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):

            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)
    speak('downloaded')
