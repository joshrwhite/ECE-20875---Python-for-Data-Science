import numpy as np
from scipy.stats import norm
from math import sqrt

#function which carries out the expectation step of expectation-maximization
def expectation(data, weights, means, varis):
    k = len(means)
    N = len(data)
    gammas = np.zeros((k,N))

    #fill in here
    #code to calculate each gamma = gammas[i][j], the likelihood of datapoint j in gaussian i, from the
    #current weights, means, and varis of the gaussians
    for i in range(k):
        for j in range(N):
            p_g = norm.pdf(data[j], means[i], sqrt(varis[i]))
            p_xj = 0
            for g in range(k):
                p_xj += norm.pdf(data[j], means[g], sqrt(varis[g])) * weights[g]
            gammas[i][j] = p_g * weights[i] / p_xj

    return gammas


#function which carries out the maximization step of expectation-maximization
def maximization(data, gammas):
    k = len(gammas)
    N = len(data)
    weights = np.zeros(k)
    means = np.zeros(k)
    varis = np.zeros(k)

    #fill in here
    #code to calculate each (i) weight = weights[i], the weight of gaussian i, (ii) mean = means[i], the
    #mean of gaussian i, and (iii) var = varis[i], the variance of gaussian i, from the current gammas of the
    #datapoints and gaussians

    for i in range(k):
        Ni = 0
        for j in range(N):
            Ni += gammas[i][j]
        weights[i] = Ni / N

        ui_num = 0
        for j in range(N):
            ui_num += gammas[i][j] * data[j]
        means[i] = ui_num / Ni

        varis_num = 0
        for j in range(N):
            varis_num += gammas[i][j] * ((data[j] - means[i]) ** 2)
        varis[i] = varis_num / Ni

    return weights, means, varis


#function which trains a GMM with k clusters until expectation-maximization returns a change in log-likelihood of less
#than a tolerance tol
def train(data, k, tol):
    # fill in
    # initializations of gaussian weights, means, and variances according to the specifications
    weights = [1/k] * k
    tmp = (max(data) - min(data)) / k
    means = [( min(data) + i * tmp) for i in range(k)]
    varis = [1] * k

    diff = float("inf")
    ll_prev = -float("inf")

    # iterate through expectation and maximization procedures until model convergence
    while(diff >= tol):
        gammas = expectation(data, weights, means, varis)
        weights, means, varis = maximization(data, gammas)
        ll = log_likelihood(data,weights,means,varis)
        diff = abs(ll - ll_prev)
        ll_prev = ll

    print(f'LL = {ll}')
    return weights, means, varis, ll


#calculate the log likelihood of the current dataset with respect to the current model
def log_likelihood(data, weights, means, varis):
    #fill in
    ll = 0
    for j in range(len(data)):
        inner = 0
        for i in range(len(weights)):
            inner += weights[i] * norm.pdf(data[j], means[i], sqrt(varis[i]))
        ll += np.log(inner)

    return ll


def main(datapath, k, tol):
    #read in dataset
    with open(datapath) as f:
        data = f.readlines()
    data = [float(x) for x in data]

    #train mixture model
    weights, means, varis, ll = train(data, k, tol)

    return weights,means,varis,ll

if __name__ == '__main__':
    main('data.txt', 3, 1)