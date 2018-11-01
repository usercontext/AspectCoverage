from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import nltk
import csv
import re

with open('data/travel/quora.txt') as f:
    words_quora = [word for line in f for word in line.split()]

with open('data/travel/wikihow.txt') as f:
    words_wiki = [re.sub(r'[^\w\s]', '', word) for line in f for word in line.split()]

with open('data/travel/stackexchange.txt') as f:
    words_stackexchange = [re.sub(r'[^\w\s]', '', word) for line in f for word in line.split()]

with open('data/travel/reddit.txt') as f:
    words_reddit = [re.sub(r'[^\w\s]', '', word) for line in f for word in line.split()]

wiki_sentence = []
for w in words_wiki:
    if w.lower() not in stop_words:
        wiki_sentence.append(w.lower())

quora_sentence = []
for w in words_quora:
    if w.lower() not in stop_words:
        quora_sentence.append(w.lower())

stackexchange_sentence = []
for w in words_stackexchange:
    if w.lower() not in stop_words:
        stackexchange_sentence.append(w.lower())

reddit_sentence = []
for w in words_reddit:
    if w.lower() not in stop_words:
        reddit_sentence.append(w.lower())

finder = TrigramCollocationFinder.from_words(wiki_sentence)
trigram_wiki = finder.nbest(TrigramAssocMeasures.likelihood_ratio, 20)
finder = TrigramCollocationFinder.from_words(quora_sentence)
trigram_quora = finder.nbest(TrigramAssocMeasures.likelihood_ratio, 20)

finder = BigramCollocationFinder.from_words(wiki_sentence)
bigram_wiki = finder.nbest(BigramAssocMeasures.likelihood_ratio, 20)
finder = BigramCollocationFinder.from_words(quora_sentence)
bigram_quora = finder.nbest(BigramAssocMeasures.likelihood_ratio, 20)

finder = BigramCollocationFinder.from_words(reddit_sentence)
bigram_reddit = finder.nbest(BigramAssocMeasures.likelihood_ratio, 20)
finder = BigramCollocationFinder.from_words(stackexchange_sentence)
bigram_stackexchange = finder.nbest(BigramAssocMeasures.likelihood_ratio, 20)

finder = TrigramCollocationFinder.from_words(reddit_sentence)
trigram_reddit = finder.nbest(TrigramAssocMeasures.likelihood_ratio, 20)
finder = TrigramCollocationFinder.from_words(stackexchange_sentence)
trigram_stackexchange = finder.nbest(TrigramAssocMeasures.likelihood_ratio, 20)

universal = trigram_wiki + bigram_wiki + trigram_quora + bigram_quora + trigram_stackexchange + bigram_stackexchange + trigram_reddit + bigram_reddit

# with open("Trigram_Quora.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(trigram_quora)

# with open("Trigram_Wiki.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(trigram_wiki)

# with open("Bigram_Quora.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(bigram_quora)

# with open("Bigram_Wiki.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(bigram_wiki)
import spacy
nlp = spacy.load('en_core_web_lg')
import math
from subprocess import Popen, PIPE


def caterr(nue):
    try:
        return int(math.ceil(((1/nue)-1)))
    except ZeroDivisionError:
        return 10


print("calculating Similarity matrix")
similarity_mat = [[nlp(' '.join(k)).similarity(nlp(' '.join(i)))
                   for k in universal] for i in universal]
distance_mat = [[caterr(k) for k in i] for i in similarity_mat]

with open("data/ddcrp/Universal_Pool.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(universal)

with open('data/ddcrp/Distance_Matrix.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(distance_mat)

print("DDCRP starting")
process = Popen(['Rscript', 'ddcrp/ddcrp.R'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stderr)

print("Cluster starting")
try:
    with open("cluster.txt", "r") as f:
        ddcrp_clust = f.readlines()

    ddcrp_clust = ddcrp_clust[1:]
    op = {}
    for i in ddcrp_clust:
        line = i.split(' ')
        if line[1] not in op:
            op[line[1]] = []
        op[line[1]].append(universal[int(line[2])-1])

    for key, value in op.items():
        val = list(set(value))
        op[key] = val

    print("Writing output")
    opfile = open("output.txt", "w")
    for key, value in op.items():
        quora_score = 0
        wiki_score = 0
        reddit_score = 0
        stackexchange_score = 0
        val_list = []
        for i in value:
            val_list.append(i)
            if i in bigram_quora or i in trigram_quora:
                quora_score += 1
            if i in bigram_wiki or i in trigram_wiki:
                wiki_score += 1
            if i in bigram_reddit or i in trigram_reddit:
                reddit_score += 1
            if i in bigram_stackexchange or i in trigram_stackexchange:
                stackexchange_score += 1

        total_score = quora_score + wiki_score + reddit_score + stackexchange_score
        # quora_prob = quora_score/(quora_score + wiki_score)
        # wiki_prob = wiki_score/(quora_score + wiki_score)
        # ent_quora = quora_prob*(math.log(quora_prob, 2)) if quora_prob != 0 else 0
        # ent_wiki = wiki_prob*(math.log(wiki_prob, 2)) if wiki_prob != 0 else 0
        # score = ent_quora + ent_wiki
        # if quora_prob == wiki_prob:
        #     lead = "Wiki + Quora"
        # elif quora_prob > wiki_prob:
        #     lead = "Quora"
        # elif quora_prob < wiki_prob:
        #     lead = "Wiki"
        score_list = {"Q": str(round(quora_score/total_score, 2)), "W": str(round(wiki_score/total_score, 2)), "R": str(round(reddit_score/total_score, 2)), "S": str(round(stackexchange_score/total_score, 2))}
        opfile.write("Score = " + str(score_list) + " --- Cluster " + str(val_list) + "\n")

except Exception as e:
    print(e)
