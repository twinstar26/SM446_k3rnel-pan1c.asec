import sys

from nltk.corpus import wordnet

sen1 = "me answers for [error](ClassName not Found)"


for syn in wordnet.synsets(sys.argv[1]):
    for name in syn.lemma_names():
        with open('result', 'a') as f:
            f.write(name + ' ' + sen1 + '\n')
            # f.write(name + ' ' + sen2 + '\n')
            # f.write(name + ' ' + sen3 + '\n')
            # f.write(name + ' ' + sen4 + '\n')


for syn in wordnet.synsets(sys.argv[2]):
    for name in syn.lemma_names():
        with open('result', 'a') as f:
            f.write(name + ' ' + sen1 + '\n')
            # f.write(name + ' ' + sen2 + '\n')
            # f.write(name + ' ' + sen3 + '\n')
            # f.write(name + ' ' + sen4 + '\n')


for syn in wordnet.synsets(sys.argv[3]):
    for name in syn.lemma_names():
        with open('result', 'a') as f:
            f.write(name + ' ' + sen1 + '\n')
            # f.write(name + ' ' + sen2 + '\n')
            # f.write(name + ' ' + sen3 + '\n')
            # f.write(name + ' ' + sen4 + '\n')
