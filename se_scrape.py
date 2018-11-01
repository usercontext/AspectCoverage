with open('data/src/user-ct-test-collection-01.txt') as f:
    data = f.readlines()

import spacy
nlp = spacy.load('en_core_web_lg')

count = 0
doc1 = nlp('travel')
doc2 = nlp('brand')
for i in data:
    doc2 = nlp(i.split('\n')[1])
    score = doc1.similarity(doc2)
    if score>0.4:
        print(count)
        count +=1

print(count)
