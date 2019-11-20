import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from gmm_em import *
import math

#function which computes a gaussian model with mean mu and variance var on the data array x
def gauss(x, mu, var):
    #fill in
    ls = list()
    for i in range(len(x)):
        ls.append(norm.pdf(x[i], mu, sqrt(var)))
    p = np.array(ls)
    return p


#function which uses plt to plot the individual clusters and the full mixture model on a single chart
def plot_model(x, clusters, model):
    #fill in

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    plt.plot(x, model, color=colors[0], label='Model')
    for i in range(len(clusters)):
        plt.plot(x, clusters[i], color=colors[i+1], label=f'K {i+1}')

    plt.legend()
    plt.grid(True)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title(f'{len(clusters)} Gaussians')
    plt.savefig(f'{len(clusters)}plot.png')
    #plt.show()
    plt.close()


def main(weights, means, varis):
    #find range of inputted mixture model to be plotted
    [gmin, gmax] = [np.argmin(means), np.argmax(means)]
    xmin = means[gmin] - 4*np.sqrt(varis[gmin])
    xmax = means[gmax] + 4*np.sqrt(varis[gmax])

    #define range of 1000 points based on xmin and xmax
    inc = (xmax - xmin) / 1000
    x = np.arange(xmin,xmax+inc,inc)

    k = len(means)
    clusters = []   #a list of each component (gaussian) in the mixture applied to the vector x
    model = np.zeros(len(x))    #total mixture model applied to the vector x
    for i in range(k):
        p_i = gauss(x,means[i],varis[i])
        clusters.append(weights[i]*p_i)
        model += weights[i]*p_i

    print(f'K = {len(weights)}')
    for i in range(len(weights)):
        print(f'\tWeight: {round(weights[i], 3)}, Varis: {round(varis[i], 2)}, Mean: {round(means[i], 2)}')
    #plot the results
    plot_model(x,clusters,model)

if __name__ == '__main__':
    with open('data.txt') as f:
        data = f.readlines()
    data = [float(x) for x in data]
    k_list = [2,3,4,5,6]
    tol = 1
    #train mixture model
    for k in k_list:
        weights, means, varis, ll = train(data, k, tol)
        main(weights, means, varis)
