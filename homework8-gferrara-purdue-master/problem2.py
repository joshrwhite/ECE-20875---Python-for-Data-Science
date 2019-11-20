from hw8_1 import *
import sys
import operator
from helper import *

if __name__ == '__main__':
    language_list = ['ngrams/english.txt', 'ngrams/french.txt', 'ngrams/german.txt', 'ngrams/italian.txt', 'ngrams/portuguese.txt', 'ngrams/spanish.txt']
    ngrams = set()
    language_freq = dict()
    for language in language_list:
        freq = getDict(language)
        language_freq[language] = freq
        sorted_freq = sorted(freq.items(), reverse=True, key=operator.itemgetter(1))
        s = set(freq.keys())
        ngrams = ngrams.union(s)
        #print(f'{language}: {len(s)}')
    sorted_ngrams = list(ngrams)
    sorted_ngrams.sort()
    #print(sorted_ngrams)

    freq_list = [0] * len(sorted_ngrams)
    for language in language_freq:
        lookup = language_freq[language]
        for i,ngram in enumerate(sorted_ngrams):
            if ngram in lookup:
                freq_list[i] = lookup[ngram]
            else:
                freq_list[i] = 0
        lang = (language.split('/'))[-1]
        filename = lang.replace('.txt', '') + '.png'
        plotHisto(freq_list, filename)
        #print(f"{filename} has been saved.")

    # language = 'ngrams/mystery.txt'
    # freq = getDict(language)
    # language_freq[language] = freq
    # sorted_freq = sorted(freq.items(), reverse=True, key=operator.itemgetter(1))
    # lookup = language_freq[language]
    # for i, ngram in enumerate(sorted_ngrams):
    #     if ngram in lookup:
    #         freq_list[i] = lookup[ngram]
    #     else:
    #         freq_list[i] = 0
    # lang = (language.split('/'))[-1]
    # filename = lang.replace('.txt', '') + '.png'
    # plotHisto(freq_list, filename)
    # print(f"{filename} has been saved.")
