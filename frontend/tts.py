# from gtts import gTTS 
# import playsound
import pyttsx3

#import os

mytext = "If you see my dad in Heaven He won't be hard to find. He'll be the one to greet you first, For he's a one-of-a-kind."

language = 'en'

def tts(mytext):
    # myobj = gTTS(text=mytext, lang=language, slow=False) 
    # myobj.save("welcome.mp3") 
    # playsound.playsound("welcome.mp3")
    engine = pyttsx3.init()
    engine.say(mytext)
    engine.setProperty('rate',120)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()

# os.system(" welcome.mp3") 
if __name__=="__main__":
    tts(mytext)