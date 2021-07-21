import networkx as nx
import numpy as np

from src.PTVA.helpers import *

def PTVA(G, observers, Ka, sigma2, mn):
    """Main Function for PTVA"""

    ## selecting t1
    t1 = G.nodes[observers[0]]['time']
    
    ##computing d
    d = delayVector(G, t1, observers)
    
    ## score
    likelihood = {}

    for s in list(G.nodes()):
        bfs = nx.bfs_tree(G, source = s)
        mu_s = mu(bfs,mn, observers,s)
        delta_s = covariance(bfs, sigma2,observers,s)
        score = np.dot(np.dot(mu_s.T, np.linalg.inv(delta_s)), d - (0.5)*mu_s)
        likelihood[s]=score
    
    sortedLikelihood = sorted(likelihood.items(), key=lambda x : x[1], reverse=True)

    for i,x in sortedLikelihood:
        print(f'The node {i} has {x[0][0]} likelihood')

    return sortedLikelihood