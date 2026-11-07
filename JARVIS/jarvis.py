import keyboard
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import sys
import time
import speedtest
import requests
from requests import get
import PyPDF2
#from playsound import playsound
#from gtts import gTTS
#from googletrans import Translator
import pyautogui
import pywhatkit

import pyjokes
from PyQt5 import QtWidgets, QtCore , QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voice", voices[0].id) #david=0, ziri= 3, ravi= 2, hemant= 1
engine.setProperty("rate", 150)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text



# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if 0 <= hour <= 12:
        speak(f"good morning,sir, its {tt}")
    elif 12 < hour < 16:
        speak(f"good afternoon,sir, its {tt}")
    else:
        speak(f"good evening,sir, its {tt}")
    speak("I am online sir. Please tell me how can I help you.")


# to read pdf
# def Reader():
#     speak("Tell me the name of book")

#     name = takecommand().lower()

#     if "hindi" in name:

#         os.startfile("C:\\Users\\HP\\Desktop\\l.pdf")
#         book = open("C:\\Users\\HP\\Desktop\\l.pdf","rb")
#         pdfreader = PyPDF2.PdfFileReader(book)
#         pages = pdfreader.getNumPages()
#         speak(f"number of pages in this book is {pages}")
#         speak("from which page I have to start reading?")
#         numPage = int(input("Enter the page number :"))
#         page = pdfreader.getPage(numPage)
#         text = page.extractText()
#         speak("in which language I have to read?")
#         lang = takecommand().lower()

#         if "hindi" in lang:
#             transl = Translator()
#             textHin = transl.translate(text, "hi")
#             textm = textHin.text
#             speech = gTTS(text = textm)
#             try:
                
#                 speech.save("book.mp3")
#                 #playsound("book.mp3")

#             except:
#                 #playsound("book.mp3")

#         else:
#             engine.setProperty("rate", 110)
#             speak(text)

    # elif "english" in name:

    #     os.startfile("C:\\Users\\HP\\Desktop\\python books\\ghvs110.pdf")
    #     book = open("C:\\Users\\HP\\Desktop\\python books\\ghvs110.pdf","rb")
    #     pdfreader = PyPDF2.PdfFileReader(book)
    #     pages = pdfreader.getNumPages()
    #     speak(f"sir, total number of pages in this book are {pages}")
    #     speak("from which page I have to start reading?")
    #     numPage = int(input("Enter the page number :"))
    #     page = pdfreader.getPage(numPage)
    #     text = page.extractText()
    #     speak("sir, in which language should I read?")
    #     lang = takecommand().lower()

    #     if "hindi" in lang:
    #         texstl = Translator()
    #         textHin = texstl.translate(text,"hi")
    #         textm = textHin.text
    #         speech = gTTS(text = textm)
    #         try:
    #             speech.save("book.mp3")
    #             playsound("book.mp3")

    #         except:
    #             playsound("book.mp3")

    #     else:
    #         speak(text)


# to youtube  search
def Youtubesearch(term):

    result = "https://www.youtube.com/results?search_self.query=" + term

    webbrowser.open(result)
    speak("Sir, there are some videos related to your search.")

    pywhatkit.playonyt(term)
    speak("Sir, this is the best video among the all. enjoy the video!")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Task()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=8, phrase_time_limit=10)

        try:
            print("Recognizing....")
            self.query = r.recognize_google(audio, language="en-in")
            print(f"user said: {self.query}")

        except Exception as e:
            speak("Say that again please....")
            return "none"
        return self.query


    def Task(self):
        wish()
        while True:

            self.query = self.takecommand().lower()

    # To open any application like notepad

            if "open notepad" in self.query:
                speak("opening notepad")
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                speak("opening adobe reader")
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "music" in self.query or "song" in self.query or "gana" in self.query:
                speak("playing music")
                time.sleep(3)
                mpath = "C:\\Users\\HP\\Music\\Video Projects\\Sunn Raha Hai -  www.songsof.net.mp3"
                os.startfile(mpath)
                sys.exit()

            elif "open command prompt" in self.query or "cmd" in self.query:
                speak("opening command prompt")
                os.system("start cmd")

            elif "open paint" in self.query:
                speak("opening paint")
                cpath = "C:\\WINDOWS\\system32\\mspaint.exe"
                os.startfile(cpath)

            elif "open typing games" in self.query:
                speak("opening typing games")
                dpath = "C:\\Program Files (x86)\\TypingMaster.exe"
                os.startfile(dpath)
                time.sleep(1)
                pyautogui.press("enter")

            elif "open whatsapp" in self.query:
                speak("opening whatsapp")
                a = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(a)

    # To close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close command prompt" in self.query:
                speak("okay sir, closing command prompt")
                os.system("taskkill /f /im cmd.exe")

            elif "close adobe reader" in self.query:
                speak("okay sir, closing Adobe reader")
                os.system("taskkill /f /im AcroRd32.exe")

            elif "close paint" in self.query:
                speak("okay sir, closing paint")
                os.system("taskkill /f /im mspaint.exe")

            elif "close typing games" in self.query:
                speak("closing typing games")
                os.system("taskill /f /im TypingMaster.exe")

    # To location, ip adress, internet speed
            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"sir, your IP address is {ip}")

            

                

            elif "where i am" in self.query or "where we are" in self.query or "location" in self.query:
                speak("sir please wait, I am checking")

                try:
                    ipAdd = requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print (geo_data)
                    city = geo_data["city"]
                    # state = geo_data["state"]
                    country = geo_data["country"]
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    webbrowser.open("https://earth.google.com/web/search/Prabhat+Nagar,+Muzaffarpur,+Bihar/@26.1150538,85.3581932,53.95080426a,937.07140109d,35y,0h,45t,0r/data=CowBGmISXAolMHgzOWVkMTBkMzg4ZDE4ODk3OjB4ZWUxMmQwZWMxMDExNzRjNxnj0kITch06QCHjpDDv8VZVQCohUHJhYmhhdCBOYWdhciwgTXV6YWZmYXJwdXIsIEJpaGFyGAIgASImCiQJVcgs0CogOkARHQRA2V0aOkAZM9h-cJVYVUAhpPI2vTlVVUAoAjoDCgEw?authuser=0")

                except Exception as e:
                    speak("sorry sir, due to network issue i am not able to find where we are.")
                    pass
                        
    # To read any book pdf
            # elif "read a book" in self.query or "book" in self.query:
            #     Reader()

    # To conversation with Jarvis
            elif "hello" in self.query:
                speak("Hello sir!, may I help you in something?")

            elif "how are you" in self.query:
                speak("I am fine sir, what about you?")

            elif "fine" in self.query or "am good" in self.query or "also good" in self.query:
                speak("It is great to hear it from you sir")

            elif "name" in self.query or "who are you" in self.query:
                webbrowser.open("https://www.google.com/search?q=jarvis&ei=5BEGYb-6EprWz7sPidqpiA8")
                speak("My name is jarvis, which means Just A Rather Very Intelligent System (J.A.R.V.I.S.) was originally Atul Kumar's natural-language user interface computer system, named after Edwin Jarvis, ...")

    # To use PyautoGui like volume up, switch window
            elif "volume up" in self.query or "increase volume" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query or "decrease volume" in self.query:
                pyautogui.press("volumedown")

            elif "volume up" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")

            elif "switch window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

    # To sleep jarvis and to wake up jarvis
            elif "can sleep" in self.query or 'sleep now' in self.query:
                speak("thanks for using me sir, have a good day ahead")
                sys.exit()

            elif "good night" in self.query:
                speak("good night sir, see you tomorrow")
                sys.exit()

    # To search anything on google, youtube
            elif "google search" in self.query:
                import wikipedia as googleScrap
                # self.query.replace("jarvis", "")
                # self.query.replace("google", "")
                # self.query.replace("Google Search", "")
                # self.query.replace("ok", "")
                pywhatkit.search(self.query.replace("ok jarvis google search",""))

                try:
                    result = googleScrap.summary(self.query,2)
                    speak(result)

                except:
                    speak(f"sir, I have no information about {self.query}.")

            elif "shopping" in self.query or "shop" in self.query:
                webbrowser.open("https://www.google.co.in/shopping?hl=en&source=og&tab=rf&authuser=0")
                speak("sir, what you want to see or buy from google shopping")
                write = self.takecommand().lower()
                time.sleep(6)
                pyautogui.write(write)
                time.sleep(2)
                keyboard.press("enter")

            elif "video" in self.query:
                # self.query = self.query.replace("jarvis","")
                # self.query = self.query.replace("can you","")
                # self.query = self.query.replace("video","")
                # self.query = self.query.replace("some","")
                # self.query = self.query.replace("show","")
                # self.query = self.query.replace("a","")
                # self.query = self.query.replace("videos","")
                # self.query = self.query.replace("one","")
                from jarvis import Youtubesearch
                Youtubesearch(self.query.replace("show""can""me""a", ""))

    # To open any online application
            elif "open youtube" in self.query:
                speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com")

            elif "open classroom" in self.query:
                speak("Opening classroom")
                webbrowser.open("https://classroom.google.com/u/1/c/MTE2MTM0NDA3Nzkx")

            elif "open gmail" in self.query:
                speak("Opening gmail")
                webbrowser.open("https://mail.google.com/mail/?tab=rm&ogbl")

            elif "open drive" in self.query:
                speak("Opening drive")
                webbrowser.open("https://drive.google.com/drive/u/1/my-drive")

            elif "open translate" in self.query or "open translator" in self.query:
                speak("Opening google translate")
                webbrowser.open("https://translate.google.co.in/?hl=en&tab=rT&sl=hi&tl=en&op=translate")

            elif "open earth" in self.query or "open map" in self.query:
                speak("sir, 3D map is opening")
                webbrowser.open("https://earth.google.com/web/@0,0,0a,22251752.77375655d,35y,0h,0t,0r/data=OgMKATA?authuser=0")


    # To sleep the system
            elif "sleep the system" in self.query or "close the system" in self.query:
                speak("as you wish, sir")
                time.sleep(1)
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 

    # To find a joke
            elif "joke" in self.query:
                joke = pyjokes.get_joke("en", "all")     
                speak(joke)  

    # To know the time, temperature, date and day
            elif "time" in self.query:
                tt = time.strftime("%I:%M %p")
                speak(f"sir, it is {tt}")
    
    # To write anything in notepad or note anything
            elif "note" in self.query:
                jpath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(jpath)
                speak("sir, what I have to note")
                write = self.takecommand().lower()
                time.sleep(2)
                pyautogui.write(write)
                time.sleep(2)
                speak("sir, the note has written")
            
    # To call anyone from whats app
            elif "call micromax" in self.query:
                atul = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WatsApp.exe"
                os.startfile(atul)
                time.sleep(6)
                pyautogui.click(x=128, y=113)
                time.sleep(3)
                pyautogui.write("Micromax")
                time.sleep(3)
                keyboard.press("enter")
                time.sleep(3)
                pyautogui.click(x=1208, y=58)
                speak("calling..... Micromax sir")

            elif "call ajit" in self.query:
                atul = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WatsApp.exe"
                os.startfile(atul)
                time.sleep(6)
                pyautogui.click(x=128, y=113)
                time.sleep(3)
                pyautogui.write("ajit chaudhary")
                time.sleep(3)
                keyboard.press("enter")
                time.sleep(3)
                pyautogui.click(x=1208, y=58)
                speak("calling..... ajit sir")

            elif "call jyoti" in self.query:
                atul = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WatsApp.exe"
                os.startfile(atul)
                time.sleep(6)
                pyautogui.click(x=128, y=113)
                time.sleep(3)
                pyautogui.write("jyoti supna")
                time.sleep(3)
                keyboard.press("enter")
                time.sleep(3)
                pyautogui.click(x=1155, y=50)
                speak("calling..... jyoti sir")



# text to speech
# To convert voice into text
# To wish
# To join class

# to read pdf
# to youtube  search