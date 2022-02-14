from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS as gt



def say(text):
    tts = gt(text=text, lang="el")
    filename = "say.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)




def audioIn():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        global user_said
        user_said = ""

        try:
            user_said = r.recognize_google(audio, language = "el-GR")
            print(user_said)
        except Exception as e:
            print ("Exception: " + str(e))
    
    return user_said


def greetUser(user_said):
    say(f"Γειά σου {user_said}")



def start():
    say("Γειά σου, με λένε Τίνα, από το Ρομποτίνα. Εσένα πως σε λένε;")
    audioIn()
    greetUser(user_said)

start()