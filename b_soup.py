from logging import exception
import webbrowser
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from captcha import clear_captcha
from comm import speak


# PERFORM A SEARCH ON GOOGLE
# ----------------------------
def googlefun(text):
    URL = "https://www.google.co.in/search?q=" + text

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        result = soup.find(class_='Z0LcW CfV8xf').get_text()
        # print(result)
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


# OPEN A WEBSITE IN BROWSER
# ------------------------------
def open_brows(query):
    temp = query.split(" ")
    for i in range(len(temp)):
        if(temp[i] == 'open'):
            src = temp[i+1]
    # try:
    URL = "https://www.google.co.in/search?q=" + src
    # URL = "https://www.google.com/recaptcha/api2/demo"

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
    # }

    driver = webdriver.Chrome()
    driver.get(URL)
    page = driver.page_source

    # page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page, "html.parser")

    # soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup, page, URL)
    try:
        result = soup.find(class_='yuRUbf').a['href']
    except:
        print("clearing")
        clear_captcha()
        result = soup.find(class_='yuRUbf').a['href']
    webbrowser.open_new_tab(result)
    speak('here it is')
    # except exception as e:
    #     print(e)
    # print(src)
