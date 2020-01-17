import speech_recognition as sr

r1= sr.Recognizer()
r2= sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now")
    #r1.adjust_for_ambient_noise(source, duration=5)
    audio = r1.listen(source, phrase_time_limit=5)  
    print('done')
    try:
        print(r1.recognize_google(audio))
    except sr.UnknownValueError:
        print('error')
    except LookupError:
        print("e")