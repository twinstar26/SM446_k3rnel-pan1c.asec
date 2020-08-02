# import spacy 
# from spacy.gold import GoldParse 
# from spacy.pipeline import EntityRecognizer 
  
# nlp = spacy.load('en_core_web_sm', entity = False, parser = False) 

content = '''
The Attendees for the meeting are: Harsh Chheda, Divy Patel, Dhwani Agarwal, Kritika Ravishankar.The meeting agenda is about the launch of Redmi 9 prime phone.Redmi 9 Prime is coming, and the smartphone will be unveiled on August 4 as Xiaomi's latest budget smartphone. Given Amazon is touting its launch as one of the Prime Day launches, the phone is pretty much confirmed to go on sale during the Prime Day sale event on August 6-7. Although Xiaomi has begun teasing the phone, the company hasn't shared much information about the phone. So, here's what we have been able to piece together from various official teasers as well as the speculation around the phone.In the previous meeting it was decided that for backend development we will be using Java instead of Python.Based on the Project Hackathon Jira Project, the issue of Merge Conflict has been resolved.
'''

# doc_list = [] 
# doc = nlp(content) 
# doc_list.append(doc) 
# gold_list = [] 
# gold_list.append(GoldParse(doc, [u'ANIMAL', u'O', u'O', u'O'])) 
  
# ner = EntityRecognizer(nlp.vocab, entity_types = ['ANIMAL', 'PERSON', 'NORP', 'FAC' , 'ORG' , 'GPE' , 'LOC' , 'PRODUCT' , 'EVENT' , 'WORK_OF_ART' , 'LAW' , 'LANGUAGE' , 'DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL'])  
# ner.update(doc_list, gold_list) 
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp(content.lower())
print([(X.text, X.label_) for X in doc.ents])
# print([(X, X.ent_iob_, X.ent_type_) for X in doc])