import numpy as np
import networkx as nx

def observedDelay(g, O):
    """Calculates observed delay w.r.t the first observer.

    Parameters:
      g : Graph
      o : observers list
    Returns:
      d : delay list
    """
    d = np.zeros(shape=(len(O) - 1, 1))
    for i in range(len(O) - 1):
        d[i][0] = g.nodes[O[i + 1]]['time'] - g.nodes[O[i]]['time']

    return d
    
def height_node(T, s, node):
    l = list(nx.all_simple_paths(T, s, node))
    if l == []:
        return 0
    else:
        return len(l[0]) - 1

def mu(T, s, O, mn):
    """Computes mu_n
    """
    constant = height_node(T, s, O[0])
    mu_n = np.zeros(shape=(len(O) - 1, 1))
    for i in range(len(O) - 1):
        mu_n[i][0] = height_node(T, s, O[i + 1]) - constant
    mu_n = mn * mu_n
    return mu_n

def delayCovariance(T, O, sigma2):
    """Calculates the delta_n
    """
    l = len(O)
    delta = np.zeros(shape=(l - 1, l - 1))
    T = T.to_undirected()
    for k in range(l - 1):
        for i in range(l - 1):
            if i == k:
                delta[k][i] = len(list(nx.all_simple_paths(T, O[0], O[k + 1]))[0]) - 1
            else:
                c1 = list(nx.all_simple_paths(T, O[0], O[k + 1]))[0]
                c2 = list(nx.all_simple_paths(T, O[0], O[i + 1]))[0]
                S = [x for x in c1 if x in c2]
                delta[k][i] = len(S) - 1
    delta = delta * (sigma2)
    return delta