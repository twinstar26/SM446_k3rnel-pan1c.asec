from pydub import AudioSegment
from pydub.utils import make_chunks
import os
from stt import listenToAudio
import spacy
from datetime import datetime
import nltk

nlp = spacy.load('en_core_web_sm')

regular_grammar = r"""
  KEYPHRASE: {<CD|JJ|JJR|JJS|NN|NNS|NNP|NNPS|RB|RBR|RBS>+} 
"""

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
    timestamp = str(datetime.now())
    print('Extracting text...')
    for chunk in chunks:
        text = listenToAudio(folderpath+"/"+chunk)
        final_text += text + " "

    final_text += '\n===\n'
    attendees, entities = get_attendees(final_text)
    for attendee in attendees:
        final_text+=attendee+"\n"
    final_text+='===\n'
    for entity in entities:
        final_text += entity.label_+" -> "+entity.text+"\n"
    final_text += '===\n'
    final_text += timestamp
    file = open("./minutes_of_meeting/"+timestamp.replace(' ', "_").replace('.', '-').replace(':', '-')+".txt", "w", encoding = 'UTF-8')
    file.write(final_text)
    file.close()
    # print(get_attendees(final_text))

def get_attendees(text):
    doc = nlp(text)
    attendees = []
    for entity in doc.ents:
        if entity.label_ == 'PERSON':
            attendees.append(entity.text)
    return attendees, doc.ents

if __name__ == '__main__':
    make_chunks_from_wav("./open-speech.wav", 10)
    create_text_from_chunks('open-speech')