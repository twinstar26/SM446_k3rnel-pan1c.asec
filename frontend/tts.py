from gtts import gTTS
import playsound

#import os

mytext = 'Hello'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, here we have marked slow=False. Which tells 
# the module that the converted audio should have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named welcome 
myobj.save("welcome.mp3") 
playsound.playsound("welcome.mp3")

# os.system(" welcome.mp3") 