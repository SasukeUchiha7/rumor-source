import numpy as np
import networkx as nx
from numpy.core.fromnumeric import shape

def delayVector(G, t1, observers):
    """Calcs delay with respect to the t1"""

    d = np.zeros(shape=(len(observers)-1,1))
    for i in range(len(observers) - 1):
        d[i][0]=G.nodes[observers[i + 1]]['time'] - t1
    return d


def nEdges(bfs, s, a):
    """ Returns list of edges from s -> a"""
    try:
        l = list(nx.all_simple_paths(bfs, s, a))[0]
        return l
    except:
        return [0]

def intersection(l1, l2):
    temp = set(l2)
    l = [x for x in l1 if x in temp]
    return len(l)-1

def mu(bfs, mn, observers, s):
    """Calcs the determinticDelay w.r.t bfs tree."""

    o1 = observers[0]
    length_o1 = len(nEdges(bfs, s, o1))
    mu_k = np.zeros(shape=(len(observers)-1,1))
    for k in range(len(observers)-1):
        mu_k[k][0] = len(nEdges(bfs,s,observers[k+1])) - length_o1
   
    return np.dot(mu_k, mn)

def covariance(bfs, sigma2, observers, s):
    """Cals the delayCovariance of the bfs tree."""
    
    o1 = observers[0]
    delta_k = np.zeros(shape=(len(observers)-1,len(observers)-1))
    for k in range(len(observers)-1):
        for i in range(len(observers)-1):
            if k==i:
                delta_k[k][i] = len(nEdges(bfs,o1, observers[k+1]))
            else:
                ne1 = nEdges(bfs, o1, observers[k+1])
                ne2 = nEdges(bfs, o1, observers[i+1])
                delta_k[k][i]= intersection(ne1, ne2)
    
    return sigma2*delta_k

