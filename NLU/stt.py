import speech_recognition as sr
# from pydub import AudioSegment

def listenToAudio(filename):
    r = sr.Recognizer()

    file_audio = sr.AudioFile(filename)
    audio_text = ""
    with file_audio as source:
        audio = r.record(source)
        try:
            audio_text = r.recognize_google(audio)
            return audio_text
        except Exception as e:
            print(str(e))
    return audio_text

if __name__ == "__main__":
    listenToAudio('./audio.wav')