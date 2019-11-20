import numpy as np
import matplotlib.pyplot as plt
from helper import *
from functools import reduce

#change a histogram of counts into a histogram of probabilities
#input: a histogram (like your histogram function creates)
#output: a normalized histogram with probabilities instead of counts
def norm_histogram(hist) :
    #fill in
    #hint: when doing your normalization, you should convert the integers
    #      in your histogram buckets to floats: float(x)
    norm_hist = [0] * len(hist)
    sum = 0
    for i in hist:
        sum += i
    for i in range(len(hist)):
        norm_hist[i] = float(hist[i]) / sum

    return norm_hist
    
#compute cross validation for one bin width
#input: a (non-normalized) histogram and a bin width
#output: the cross validation score (J) for the specified width
def crossValid (histo, width) :
    #1. build the list of probabilities
    norm_hist = norm_histogram(histo)
    #2. compute the sum of the squares of the probabilities
    for i in range(len(norm_hist)):
        norm_hist[i] = norm_hist[i] ** 2
    p_sum = sum(norm_hist)
    #3. determine the total number of points in the histogram
    #   hint: look up the Python "sum" function
    num_points = sum(histo)
    #4. Compute J(h) and return it
    denom = (num_points - 1) * width
    J = 2/denom - ((num_points + 1) * p_sum)/denom

    return J
    
#sweep through the range [min_bins, max_bins], compute the cross validation
#score for each number of bins, and return a list of all the Js
#Note that the range is inclusive on both sides!
#input: the dataset to build a histogram from
#       the minimum value in the data set
#       the maximum value in the data set
#       the smallest number of bins to test
#       the largest number of bins to test
#output: a list (of length max_bins - min_bins + 1) of all the appropriate js
def sweepCross (data, minimum, maximum, min_bins, max_bins) :
    #fill in. Don't forget to convert from a number of bins to a width!
    length = len(data)
    js = []
    #range(1,length+1)
    for i in range(min_bins, max_bins+1):
        hist = histogram(data, i, minimum, maximum)
        width = (maximum - minimum) / i
        js.append(crossValid(hist,width))
    return js
        
#return the minimum value in a list *and* the index of that value
#input: a list of numbers
#output: a tuple with the first element being the minimum value, and the second 
#        element being the index of that minumum value (if the minimum value is 
#        in the list more than once, the index should be the *first* occurence 
#         of that minimum value)
def findMin (l) :
    minVal = l[0]
    minIndex = 0
    for i in range(len(l)):
        if l[i] < minVal:
            minVal = l[i]
            minIndex = i

    return (minVal, minIndex)


if __name__ == '__main__':
    # Sample test code
    data = getData()  # reads data from inp.txt
    lo = min(data)
    hi = max(data)

    js = sweepCross(data, lo, hi, 1, 100)
    print(findMin(js))