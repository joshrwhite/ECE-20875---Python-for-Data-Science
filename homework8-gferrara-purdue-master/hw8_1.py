#Arguments:
#  filename: name of file to read in
#Returns: a list of strings, each string is one line in the file
#hints: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       https://docs.python.org/3/library/stdtypes.html#str.splitlines
def getText(filename) :
    #fill in
    ls = list()
    with open(filename, "r") as file:
        r = file.read()
        l = r.splitlines()
    return l

#Arguments:
#  line: a string of text
#Returns: a list of n-grams
#Notes: make sure to pad the beginning and end of the string with '_'
#       make sure to convert the string to lower-case
#       so "Hello" should be turned into "__hello__" before processing
def getNgrams(line) :
    s = line.lower()
    s = '__' + s + '__'
    ngram_list = list()
    for i in range(len(s) -2):
        ngram = s[i:(i+3)]
        ngram_list.append(ngram)

    return ngram_list


#Arguments:
#  filename: the filename to create an n-gram dictionary for
#Returns: a dictionary, with ngrams as keys, and frequency of that ngram as the value.
#Notes: Remember that getText gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       use 'map', use getText, and use getNgrams
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def getDict(filename) :
    #fill in
    lines = getText(filename)
    freq = dict()
    for i in range(len(lines)):
        ls = getNgrams(lines[i])
        for n in ls:
            if n in freq: freq[n] += 1
            else: freq[n] = 1
    return freq
