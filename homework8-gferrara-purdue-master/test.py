from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import numpy as np


x = np.array([[3,2,0,1],[4,1,2,5]])
y = np.argsort(a=-x, axis=1)
print(y)