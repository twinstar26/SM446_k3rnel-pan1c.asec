import sys

from nltk.corpus import wordnet

sen1 = "me public repositories of [userName](atharvaveer) workspace"
sen2 = "me public repositories of [userName](atharvaveer)"


for syn in wordnet.synsets(sys.argv[1]):
    for name in syn.lemma_names():
        with open('result', 'a') as f:
            f.write(name + ' ' + sen1 + '\n')
            f.write(name + ' ' + sen2 + '\n')