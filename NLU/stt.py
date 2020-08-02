import speech_recognition as sr
# from pydub import AudioSegment

<<<<<<< HEAD
def listenToAudio(filename):
    print(sr.__version__)
=======
def listenToAudio():
    # print(sr.__version__)
>>>>>>> 15f437db716522765d1b4fb28faa4f6389cd5ae1
    r = sr.Recognizer()

    #     # convert mp3 file to wav
    # sound = AudioSegment.from_mp3("./audio.mp3")
    # sound.export("./audio.wav", format="wav")

<<<<<<< HEAD
    file_audio = sr.AudioFile(filename)
    print(file_audio)
    # audio = ""
=======
    file_audio = sr.AudioFile('audio.wav')
    # print(file_audio)
    audio_text = ""
>>>>>>> 15f437db716522765d1b4fb28faa4f6389cd5ae1
    with file_audio as source:
        # r.adjust_for_ambient_noise(source)
        audio = r.record(source)

        try:
            audio_text = r.recognize_google(audio)
<<<<<<< HEAD
            return audio_text
=======
            print(audio_text)
>>>>>>> 15f437db716522765d1b4fb28faa4f6389cd5ae1
        except Exception as e:
            print(str(e))
    return audio_text

if __name__ == "__main__":
    listenToAudio()