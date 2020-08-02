import speech_recognition as sr
# from pydub import AudioSegment

def listenToAudio(filename):
    print(sr.__version__)
    r = sr.Recognizer()

    #     # convert mp3 file to wav
    # sound = AudioSegment.from_mp3("./audio.mp3")
    # sound.export("./audio.wav", format="wav")

    file_audio = sr.AudioFile('audio.wav')
    # print(file_audio)
    audio_text = ""
    with file_audio as source:
        # r.adjust_for_ambient_noise(source)
        audio = r.record(source)

        try:
            audio_text = r.recognize_google(audio)
            return audio_text
        except Exception as e:
            print(str(e))
    return audio_text

if __name__ == "__main__":
    listenToAudio()