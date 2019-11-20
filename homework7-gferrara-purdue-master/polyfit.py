import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of n = degrees[i].
def main(datapath, degrees):
    paramFits = []
    X = list()
    Y = list()
    x_data = list()
    #read the input file, assuming it has two columns, where each row is of the form [x y] as in problem1.txt.
    with open('poly.txt', "r") as file:
        lines = file.readlines()
        for line in lines:
            nums = line.split()
            x = float(nums[0])
            y = float(nums[1])
            x_data.append(float(nums[0]))
            X.append(float(nums[0]))
            Y.append(y)

    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.

    for i in degrees:
        X_n = feature_matrix(X, i)
        B = least_squares(X_n, Y)
        paramFits.append(B)


    plt.scatter(x_data, Y, color = 'k', marker='o', label='Given')
    plt.xlabel('X-Data')
    plt.ylabel('Y-Data')
    plt.grid(True)
    
    colors = ['b', 'g', 'r', 'c', 'm']
    markers = ['+', 'x', 'd', 's', '.']

    x_data.sort()
    for n in range(len(degrees)):
        y_n = list()
        y_n_mse = 0
        for point in x_data:
            sum = 0
            for i in range(len(paramFits[n])):
                count = paramFits[n][i] * (point ** (len(paramFits[n]) - (i + 1)))
                sum += count
            y_n.append(sum)
        for i in range(len(Y)):
            dif = (y_n[i] - Y[i]) ** 2
            y_n_mse += dif
            #y_1_msd.append(dif)
        print(f'MSE Degree {degrees[n]}: {y_n_mse}')
        for i in range(n+1):
           print(f'x^{degrees[n] - i}*{paramFits[n][i]} + ', end='')
        print(paramFits[n][-1])
        plt.plot(x_data, y_n, color=colors[n], marker=markers[n], label=f'Degree {degrees[n]}')
    plt.legend()
    plt.show()

    x_data2 = [2]
    y_n = list()
    y_n_mse = 0
    for point in x_data2:
        sum = 0
        for i in range(len(paramFits[n])):
            count = paramFits[n][i] * (point ** (len(paramFits[n]) - (i + 1)))
            sum += count
        y_n.append(sum)



    return paramFits



#Return the feature matrix for fitting a polynomial of degree n based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and n as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by n+1.
def feature_matrix(x, n):
    X = list()
    for i in range(len(x)):
        x_n = [ x[i] ** (n-j) for j in range(n) ]
        x_n.append(1)
        X.append(x_n)
    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^n, x^(n-1), ..., x^0.

    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    #fill in
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.transpose(X)), y)


    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [1,2,3,4,5]

    paramFits = main(datapath, degrees)
    print(paramFits)
