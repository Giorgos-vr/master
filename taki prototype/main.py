from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS as gt

r = sr.Recognizer()

# Words that sphinx should listen closely for. 0-1 is the sensitivity
# of the wake word.
keywords = [("tacky", 0.9), ("blue", 1), ]

source = sr.Microphone()

def audioIn():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            user_said = ""
            

            try:
                user_said = r.recognize_google(audio, language = "el-GR")
                print(user_said)
            except sr.UnknownValueError:
                say("Δεν σε κατάλαβα, συγνώμη!")
                pass
            except sr.RequestError:
                say("Αδυναμία σύνδεσης!")
                pass
        
        return user_said

def callback(recognizer, audio):

    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)

        # Look for keyword in speech_as_text
        if "tacky" in speech_as_text or "blue":
            audioIn()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def say(text):
        tts = gt(text=text, lang="el")
        filename = "say.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)




def start_recognizer():
    r.listen_in_background(source, callback)
    time.sleep(1000000)


start_recognizer()
#test