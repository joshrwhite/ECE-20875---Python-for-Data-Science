from hw8_1 import *
import sys
import operator

if __name__ == '__main__':
    freq = getDict(sys.argv[1])
    sorted_freq = sorted(freq.items(), reverse=True, key=operator.itemgetter(1))
    top10 = sorted_freq[0:10]
    #print("Spanish.txt:")
    print(top10)


    # freq = getDict('ngrams/portuguese.txt')
    # sorted_freq = sorted(freq.items(), reverse=True, key=operator.itemgetter(1))
    # top10 = sorted_freq[0:10]
    # print("\nPortuguese.txt:")
    # print(top10)
    #
    # freq = getDict('ngrams/mystery.txt')
    # sorted_freq = sorted(freq.items(), reverse=True, key=operator.itemgetter(1))
    # top10 = sorted_freq[0:10]
    # print("\nMystery.txt:")
    # print(top10)



