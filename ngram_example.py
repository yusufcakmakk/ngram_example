import os
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import preprocessing as pp

with open("tokenized_data.txt", "r", encoding="UTF-8") as f:
    lines = [pp.apply_preprocess(line.strip(), deascify=False) for line in f.readlines()]

frequencies_unigram = {}
frequencies_bigram = {}
frequencies_trigram = {}
frequencies_fourgram = {}

for text in lines:
    if text.strip() == "" or len(text.strip()) < 4:
        continue
    else:
        token = nltk.word_tokenize(text)
        for tk in token:
            if tk in frequencies_unigram:
                frequencies_unigram[tk] += 1
            else:
                frequencies_unigram[tk] = 1
        bigrams = ngrams(token, 2)
        for tk in bigrams:
            if tk in frequencies_bigram:
                frequencies_bigram[tk] += 1
            else:
                frequencies_bigram[tk] = 1
        trigrams = ngrams(token, 3)
        for tk in trigrams:
            if tk in frequencies_trigram:
                frequencies_trigram[tk] += 1
            else:
                frequencies_trigram[tk] = 1
        fourgrams = ngrams(token, 4)
        for tk in fourgrams:
            if tk in frequencies_fourgram:
                frequencies_fourgram[tk] += 1
            else:
                frequencies_fourgram[tk] = 1

topn_count = 10

topn_unigrams = sorted(frequencies_unigram.items(), key=lambda x: x[1], reverse=True)[0:topn_count]
topn_bigrams = sorted(frequencies_bigram.items(), key=lambda x: x[1], reverse=True)[0:topn_count]
topn_trigrams = sorted(frequencies_trigram.items(), key=lambda x: x[1], reverse=True)[0:topn_count]
topn_fourgrams = sorted(frequencies_fourgram.items(), key=lambda x: x[1], reverse=True)[0:topn_count]

def save_topn_ngrams(ngram_list, file_name, n=-1):
    text_list = []
    for item in ngram_list:
        row = str(item[-1]) + "," + (item[0] if n == 1 else " ".join(item[0]))
        text_list.append(row)
    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(text_list))


save_topn_ngrams(topn_unigrams,"top_unigrams", n=1)
save_topn_ngrams(topn_bigrams,"top_bigrams")
save_topn_ngrams(topn_trigrams,"top_trigrams")
save_topn_ngrams(topn_fourgrams,"top_fourgrams")
