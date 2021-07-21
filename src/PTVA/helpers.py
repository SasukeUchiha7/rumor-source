import numpy as np
import networkx as nx
from numpy.core.fromnumeric import shape

def delayVector(G, t1, observers):
    d = np.zeros(shape=(len(observers)-1,1))
    for i in range(len(observers) - 1):
        d[i][0]=G.nodes[observers[i + 1]]['time'] - t1
    return d


def nEdges(bfs, s, a):
    l = list(nx.all_simple_paths(bfs, s, a))[0]
    return len(l)

def intersection(l1, l2):
    temp = set(l2)
    l = [x for x in l1 if x in temp]
    return len(l)

def mu(bfs, mn, observers, s):

    o1 = observers[0]
    length_o1 = nEdges(bfs, s, o1)
    mu_k = np.zeros(shape=(len(observers)-1,1))
    for k in range(len(observers)-1):
        mu_k[k][0] = nEdges(bfs,s,observers[k+1]) - length_o1
   
    return np.dot(mu_k, mn)

def covariance(bfs, sigma2, observers, s):

    o1 = observers[0]
    delta_k = np.zeros(shape=(len(observers)-1,len(observers)-1))
    for k in range(len(observers)-1):
        for i in range(len(observers)-1):
            if k==i:
                delta_k[k][i] = nEdges(bfs,o1, observers[k+1])
            else:
                ne1 = list(nx.all_simple_paths(bfs, o1, observers[k+1]))[0]
                ne2 = list(nx.all_simple_paths(bfs, o1, observers[i+1]))[0]
                # ne1 = nEdges(bfs, o1, observers[k+1])
                # ne2 = nEdges(bfs, o1, observers[i+1])
                delta_k[k][i]= intersection(ne1, ne2)
    
    return sigma2*delta_k

