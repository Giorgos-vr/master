import os
import playsound
import speech_recognition as sr
from gtts import gTTS as gt


class Command:

    def __init__(self):
        Command.user_said = ""
        Command.user_name = ""
        Command.sel = ""
        self.bad_read = False

    
    def say(text):
        tts = gt(text=text, lang="el")
        filename = "say.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)




    def audioIn():
        Command.bad_read = False
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            

            try:
                Command.user_said = r.recognize_google(audio, language = "el-GR")
                # print(Command.user_said)
            except sr.UnknownValueError:
                Command.say("Δεν σε κατάλαβα!")
                Command.user_said = ""
                Command.bad_read = True
            except sr.RequestError:
                Command.user_said = ""
                Command.bad_read = True
                Command.say("Αδυναμία σύνδεσης!")
        return Command.user_said


    def greetUser():
        if Command.bad_read is True:
            Command.user_name = None
        else:
            Command.user_name = Command.user_said
            Command.say(f"Γειά σου {Command.user_name}")
        
        return Command.user_name



    def start():
        Command.say("Γειά σου, με λένε Τίνα, από το Ρομποτίνα. Εσένα πως σε λένε;")
        Command.audioIn()
        Command.greetUser()

    def gameSelection():
        if Command.user_name != None:
            Command.say(f"{Command.user_name} ποιό παιχνίδι θέλεις να παίξουμε?")
        else:
            Command.say("Ποιό παιχνίδι θέλεις να παίξουμε?")

        input = Command.audioIn().lower().split(' ')
        #print(input)
        shapeSelect = ["σχήμα", "σχήματα", "σχηματάκι", "σχηματάκια", "χρώματα", "χρωματάκια"]
        itemSelect = ["αντικείμενα", "πράγματα", "φρούτα", "φρουτάκια", "ζώα", "ζωάκια"]
        letterSelect = ["γράμμα", "γράμματα", "γραμματάκια", "γραμματάκι", "άλφα", "βήτα", "αλφαβήτα"]
        numberSelect = ["νούμερο", "νούμερα", "αριθμός", "αριθμοί", "αριθμούς"]
        if any(word in input for word in shapeSelect):
            Command.say("Πάμε για σχήματα και χρώματα!")
            Command.sel = "shapes"
        elif any(word in input for word in itemSelect):
            Command.say("Πάμε για αντικείμενα και ζώα!")
            Command.sel = "items"
        elif any(word in input for word in letterSelect):
            Command.say("Πάμε για γράμματα!")
            Command.sel = "letters"
        elif any(word in input for word in numberSelect):
            Command.say("Πάμε για αριθμούς!")
            Command.sel = "numbers"
        else:
            Command.say("Αν θέλεις διάλεξε από το μενού!")
            Command.sel = None

        return Command.sel

    def introMenu():
        if Command.bad_read == False:
            Command.say(f"{Command.user_name} θέλεις να παίξουμε?")
        else:
            Command.say("θα ήθελες να παίξουμε?")
        input = Command.audioIn()
        if Command.bad_read == False:
            select = input.lower().split(' ')
            #print(select)
            positive_input = ["ναι", "αμέ", "αχά"]
            if any(word in select for word in positive_input):
                Command.say("Τέλεια!")
                Command.gameSelection()
            else:
                Command.say("Κρίμα!")
                Command.sel = None
                #print("bad or no input")
                return Command.sel
        else:
            #print("bad or no input")
            Command.say("Αν θέλεις διάλεξε από το μενού!")
            Command.sel = None
            return Command.sel


