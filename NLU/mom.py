from pydub import AudioSegment
from pydub.utils import make_chunks
import os
from stt import listenToAudio

def make_chunks_from_wav(filepath, chunk_time):
    myaudio = AudioSegment.from_file(filepath , "wav")
    chunk_length_ms = chunk_time*1000
    chunks = make_chunks(myaudio, chunk_length_ms)

    filename = filepath.split(".wav")[0]
    try:
        os.mkdir(filename)
    except(FileExistsError):
        pass

    os.chdir(filename)
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{1}.wav".format(filename, i)
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")
    os.chdir("../")

def create_text_from_chunks(folderpath):
    chunks = os.listdir('./'+folderpath)
    final_text = ""
    print('Extracting text...')
    for chunk in chunks:
        text = listenToAudio(folderpath+"/"+chunk)
        final_text += text + " "
    file = open(folderpath+".txt", "w", encoding = 'UTF-8')
    file.write(final_text)

if __name__ == '__main__':
    make_chunks_from_wav("./open-speech.wav", 10)
    create_text_from_chunks('open-speech')