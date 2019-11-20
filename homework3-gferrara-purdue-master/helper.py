import numpy as np
import matplotlib.pyplot as plt

#bars: list of length number of bins, with each entry having its histogram value
#filename: file to save plot to (in .png format)
#minrange: minimum value of leftmost bin
#maxrange: maximum value of rightmost bin

def plotHisto (bars, filename, minrange = 0.0, maxrange = 100.0, plotinline = False) :
	mrange = maxrange - minrange
	binsize = mrange/len(bars)
	
	#this is a "list comprehension" -- it's a quick way to process one
	#list to produce another list
	labels = [(mrange / len(bars)) * i + minrange for i in range(len(bars))]
	
	plt.bar(labels, bars, align = 'edge', width = binsize)
	if plotinline :
		plt.show()
	else :
		plt.savefig(filename)
		# plt.show()
		plt.clf()

def getData(filename = 'inp.txt') :
    return np.loadtxt(filename)

def histogram(data,n,l,h):
    if(not(type(n) == int) or n < 1):
        print('n must be a positive integer!')
        return []
    elif(l >= h):
        print('l must be less than h!')
        return []
    w = (float(h)-float(l)) / n
    hist = [0] * n
    for d in data:
        if(d < l or d > h):
            continue
        elif (d == h):
            hist[len(hist) - 1] += 1
        else:
            hist[int((d-l) / w)] += 1
    return hist