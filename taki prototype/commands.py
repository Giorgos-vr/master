from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS as gt


class command:
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
                command.user_said = r.recognize_google(audio, language = "el-GR")
                print(command.user_said)
            except sr.UnknownValueError:
                command.say("Δεν σε κατάλαβα, συγνώμη!")
            except sr.RequestError:
                command.say("Αδυναμία σύνδεσης!")
        
        return command.user_said


    def greetUser():
        user_said = command.user_said
        command.say(f"Γειά σου {user_said}")



    def start():
        command.say("Γειά σου, με λένε Τίνα, από το Ρομποτίνα. Εσένα πως σε λένε;")
        command.audioIn()
        command.greetUser()
