from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS as gt


class Command:
    user_said = ""

    
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
            

            try:
                Command.user_said = r.recognize_google(audio, language = "el-GR")
                print(Command.user_said)
            except sr.UnknownValueError:
                Command.say("Δεν σε κατάλαβα, συγνώμη!")
            except sr.RequestError:
                Command.say("Αδυναμία σύνδεσης!")
        
        return Command.user_said


    def greetUser():
        user_said = Command.user_said
        Command.say(f"Γειά σου {user_said}")



    def start():
        Command.say("Γειά σου, με λένε Τίνα, από το Ρομποτίνα. Εσένα πως σε λένε;")
        Command.audioIn()
        Command.greetUser()
