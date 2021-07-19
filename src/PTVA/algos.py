import networkx as nx
import numpy as np

from src.PTVA.helpers import *

def PTVA() -> None:
    """Main Function for PTVA.
    """

    t1 = observers[0]
    d = delayVector(g.nodes, t1)
    likelihood = {}
    for s in list(g.nodes):
        bfs = nx.bfs_tree(g, source = s)
        mu = meanss(bfs)
        delta = covariance(bfs)
        sourceLikelihood = np.dot(np.dot(mu.T, np.linalg.inv(delta)), d[s] - (1/2)*mu)
        likelihood[s]=sourceLikelihood
    
    sortedLikelihood = sorted(likelihood, key=lambda x : x[1], reverse=True)

    return sortedLikelihood