from collections import Counter
from math import sqrt

def word2vec(word):
    # count the characters in word
    cw = Counter(word)
    # precomputes a set of the different characters
    sw = set(cw)
    # precomputes the "length" of the word vector
    lw = sqrt(sum(c*c for c in cw.values()))

    # return a tuple
    return cw, sw, lw

def cosdis(v1, v2):
    # which characters are common to the two words?
    common = v1[1].intersection(v2[1])
    # by definition of cosine distance we have
    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]


# list_A = ['hashhhhhh']
# list_B = ['yash_jain', 'harsh_chheda', 'divy', 'kritika', 'josh', 'bhayander', 'dhwani', 'pakhre', 'sakhre', 'ysjfh', 'james', 'bond']
def get_most_similar(list_A, list_B):
    max = 0
    ans = ''
    threshold = 0.80     # if needed
    for key in list_A:
        for word in list_B:
            try:
                # print(key)
                # print(word)
                res = cosdis(word2vec(word), word2vec(key))
                # print(res)
                # print("The cosine similarity between : {} and : {} is: {}".format(word, key, res*100))
                if (res*100 > max):
                    max = res*100
                    ans = word
                    # print("The cosine similarity between : {} and : {} is: {}".format(word, key, res*100))
                # if res > threshold:
                #     print("Found a word with cosine distance > 80 : {} with original word: {}".format(word, key))
            except IndexError:
                pass

    return ans , max




# --------------------------------------------------------------------------------------------------------------------

# import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def vect_cos(vect, test_list):
#     """ Vectorise text and compute the cosine similarity """
#     query_0 = vect.transform([' '.join(vect.get_feature_names())])
#     query_1 = vect.transform(test_list)
#     cos_sim = cosine_similarity(query_0.A, query_1.A)  # displays the resulting matrix
#     return query_1, np.round(cos_sim.squeeze(), 3)

# # Train the vectorizer
# vocab=['hash']
# vectoriser = CountVectorizer().fit(vocab)
# print(vectoriser.vocabulary_) # show the word-matrix position pairs

# # Analyse  list_1
# list_1 = ['yash_jain', 'harsh_chheda', 'divy', 'kritika', 'josh', 'bhayander', 'dhwani', 'pakhre', 'sakhre', 'ysjfh', 'james', 'bond']
# list_1_vect, list_1_cos = vect_cos(vectoriser, [' '.join(list_1)])

# # Analyse list_2
# list_2 = ['yashh']
# list_2_vect, list_2_cos = vect_cos(vectoriser, [' '.join(list_2)])

# print('\nThe cosine similarity for the first list is {}.'.format(list_1_cos))
# print('\nThe cosine similarity for the second list is {}.'.format(list_2_cos))

# from scipy.spatial import distance
# list1 = ['yash_jain', 'harsh_chheda', 'divy', 'kritika', 'josh', 'bhayander', 'dhwani', 'pakhre', 'sakhre', 'ysjfh', 'james', 'bond']
# list2 = ['hash']
# for l in list1:
#     for ll in list2:
#         print(distance.cosine(word2vec(l),word2vec(ll)))