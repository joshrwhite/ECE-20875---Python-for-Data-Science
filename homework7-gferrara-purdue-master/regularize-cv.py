import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


def main():
    #Importing dataset
    diamonds = pd.read_csv('diamonds.csv')

    #Feature and target matrices
    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]
    y = diamonds[['price']]

    #Normalizing X
    X = normalize(X)

    #Training and testing split, with 25% of the data reserved as the test set
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    #Define the range of lambda to test
    lmbda = list()
    for i in range(0,10):
        lmbda.append(i / 10)
    for i in range(0,18):
        lmbda.append(1 + i*0.5)
    for i in range(0,91):
        lmbda.append(10 + i)
    #lmbda = [1,100]
    MODEL = []
    MSE = []
    for l in lmbda:
        #Train the regression model using a regularization parameter of l
        model = train_model(X_train,y_train,l)

        #Evaluate the MSE on the test set
        mse = error(X_test,y_test,model)

        #Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    #Plot the MSE as a function of lmbda
    #plt #fill in
    plt.scatter(lmbda, MSE, color='g', marker='x')
    plt.xlabel('Regularization Parameter')
    plt.ylabel('Mean Squared Error')
    plt.title('Regularization Effect on Measured Error')
    plt.grid(True)
    plt.show()

    #Find best value of lmbda in terms of MSE
    ind = MSE.index(min(MSE))
    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]

    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))

    coefs = model_best.coef_

    for i in coefs:
        s = f'x*{i} + '
        print(s, end="")

    sum = 0
    coefs = [5109.57820956, -201.40017969, -208.10630317, -1334.00058151, 222.31650455, -68.47863175, 501.7645397, 74.36879296]
    x_in = [0.25, 3, 3, 5, 60, 55, 4, 33, 2]
    for i in range(len(coefs)):
        sum += x_in[i] * coefs[i]
    print(sum)


    return model_best


#Function that normalizes features to zero mean and unit variance.
#Input: Feature matrix X.
#Output: X, the normalized version of the feature matrix.
def normalize(X):
    #fill in
    '''
    Xtmp = list()
    for i in X:
        ls = list()
        sum = 0
        count = 0
        for j in X[i]:
            sum += j
            count += 1
            ls.append(j)
        arr = np.array(ls)
        stddev = np.std(arr)
        avg = np.mean(arr)
        for j in range(len(ls)):
            tmp = X.loc[j, i]
            #X.loc[j,i] = (tmp - avg) / stddev
            ls[j] = (ls[j] - avg) / stddev
        Xtmp.append(ls)
    normalized_df = (X - X.mean()) / X.std()
    '''

    result = X.copy()
    for feature_name in X.columns:
        result[feature_name] = (X[feature_name] - X[feature_name].mean()) / (X[feature_name].std())

    return result


#Function that trains a ridge regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model.
def train_model(X,y,l):

    #fill in
    reg = linear_model.Ridge(alpha=l, fit_intercept=True)
    model = reg.fit(X, y)
    return model


#Function that calculates the mean squared error of the model on the input dataset.
#Input: Feature matrix X, target variable vector y, numpy model object
#Output: mse, the mean squared error
def error(X,y,model):

    #Fill in
    mse = mean_squared_error(y, model.predict(X))
    return mse

if __name__ == '__main__':
    main()