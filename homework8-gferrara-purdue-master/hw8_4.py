from helper import remove_punc
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import numpy as np
import math
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words lemmatized
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :

    #1. Open document, read text into *single* string
    with open(doc, "r") as file:
        text = file.read()

    #2. Tokenize string using nltk.tokenize.word_tokenize
    text = word_tokenize(text)

    #3. Filter out punctuation from list of words (use remove_punc)
    text = remove_punc(text)
    #4. Make the words lower case

    #text = rm_punch.lower()
    for i, word in enumerate(text):
        text[i] = text[i].lower()

    #5. Filter out stopwords
    stop_set = stopwords.words('english')
    text_nostop = [n for n in text if not n in stop_set]

    #6. Lemmatize words
    lmtzr = WordNetLemmatizer()
    words = [lmtzr.lemmatize(x) for x in text_nostop]

    return words


    #Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    wordset = set()
    wordlist = list()
    wordlist_bydoc = list()
    freqlist_bydoc = list()
    for i in doclist:
        ls = set()
        freq = dict()
        words = readAndCleanDoc(i)
        for w in words:
            if not w in wordset: wordlist.append(w)
            wordset.add(w)
            ls.add(w)
            if w in freq: freq[w] += 1
            else: freq[w] = 1
        wordlist_bydoc.append(ls)
        freqlist_bydoc.append(freq)
    #2. Use these word lists to build the doc word matrix
    docword = list()
    for i, doc in enumerate(doclist):
        row = list()
        for w in wordlist:
            lookup = freqlist_bydoc[i]
            if w in wordlist_bydoc[i]: row.append(lookup[w])
            else: row.append(0)
        docword.append(row)
    docword = np.array(docword)
    return docword, wordlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    numRows = docword.shape[0]
    numCols = docword.shape[1]
    rowSum = np.sum(docword, axis=1)
    tf = list()
    for i in range(numRows):
        ls = list()
        for j in range(numCols):
            elem = docword.item(i,j)
            ls.append(elem / rowSum[i])
        tf.append(ls)
    tf = np.array(tf)
    return tf
    
#Builds an inverse document frequency matrixfor j in range(numCols):

#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    idf = list()
    numRows = docword.shape[0]
    numCols = docword.shape[1]
    colSum = np.sum(docword, axis=0)
    for i in range(numCols):
        count = 0
        for j in range(numRows):
            if docword[j][i] > 0: count += 1
        elem = math.log10(numRows / count)
        idf.append(elem)
    idf = np.array(idf)
    idf = idf.reshape(1,len(idf))
    #fill in
    
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :

    numRows = docword.shape[0]
    numCols = docword.shape[1]
    tf = buildTFMatrix(docword)
    idf = buildIDFMatrix(docword)
    tfidf = list()
    for i in range(numRows):
        ls = list()
        for j in range(numCols):
            tf1 = tf[i][j]
            idf1 = idf[0][j]
            ls.append(tf1 * idf1)
        tfidf.append(ls)
    tfidf = np.array(tfidf)

    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html

    tfidf = buildTFIDFMatrix(docword)
    sorted = np.argsort(a=-tfidf, axis=1)
    for i,filename in enumerate(doclist):
        #ls = [docword[i][sorted[i][0]], docword[i][sorted[i][1]], docword[i][sorted[i][2]]]
        ls = [wordlist[sorted[i][0]], wordlist[sorted[i][1]], wordlist[sorted[i][2]]]
        distinctiveWords[filename] = ls

    return distinctiveWords

if __name__ == '__main__':

    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc('lecs/1_vidText.txt')[0:5])

    print("*** Testing buildDocWordMatrix ***")
    doclist = ['lecs/1_vidText.txt', 'lecs/2_vidText.txt']
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])

    print("*** Testing buildTFMatrix ***")
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis=1))

    print("*** Testing buildIDFMatrix ***")
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])

    print("*** Testing buildTFIDFMatrix ***")
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])

    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))
    pass
