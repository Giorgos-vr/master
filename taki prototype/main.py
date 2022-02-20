#fresh look...

import time

import speech_recognition as sr


r = sr.Recognizer()                    
keyword = "taki"                                                                
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    if  r.recognize_google(audio) == keyword:
        print("taki")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))