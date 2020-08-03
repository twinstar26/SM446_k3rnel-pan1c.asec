
import nltk
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet as wn
from string import punctuation

def synonyms(word, pos_tag):
  return list(
    {
      lemma.replace("_"," ").replace("-"," ") for synset in wn.synsets(
        _clean_word(word),
        pos_tag,
      ) for lemma in synset.lemma_names()
    }
  )

def _clean_word(word):
  return word.lower().strip(punctuation)

def _tokenise(sentence):
  return nltk.word_tokenize(sentence)

def _infer_pos_tags(tokens):
  return [
    (
      token,
      _convert_nltk_to_wordnet_tag(nltk_tag)
    ) for token,nltk_tag in nltk.pos_tag(tokens)
  ]

def _convert_nltk_to_wordnet_tag(pos_tag):
  if pos_tag.startswith("N"):
    return wn.NOUN
  if pos_tag.startswith("V"):
    return wn.VERB
  if pos_tag.startswith("R"):
    return wn.ADV
  if pos_tag.startswith("J"):
    return wn.ADJ

def synonymous(examples, include_verbs = True):
  synonymous = []
  for example in examples:
    for idx,sentence in enumerate(example):
      tokens = _tokenise(sentence)
      tagged_words = _infer_pos_tags(tokens)
      for jdx,word_pos in enumerate(tagged_words):
        word, pos_tag = word_pos
        if pos_tag and (include_verbs or pos_tag != "v"):
          for synonym in synonyms(word, pos_tag):
              new_tokens = tokens[:jdx] + [synonym] + tokens[jdx+1:]
              new_sentence = ' '.join(new_tokens)
              new_example = example[:idx] + [new_sentence] + example[idx+1:]
              synonymous.append(new_example)
  return synonymous

# token = _tokenise("Give me pull-request made by josh")
# print(_infer_pos_tags(token))

# res = (synonymous([["Give me pull-request made by josh"]]))

# file = open('op.txt', 'w')

# for r in res:
#   for rr in r:
#     file.write("  " + "-" + " " +rr + "\n")

