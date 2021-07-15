import numpy as np
import networkx as nx

def observedDelay(g, O):
    """Calculates observed delay.

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

def deterministicDelay(T, s, O, mi):
    """
    Computes mu_s
    :param T: tree
    :param s: source
    :param O: list of observers
    :param mi: mean
    :return:
    """
    constant = height_node(T, s, O[0])
    mi_s = np.zeros(shape=(len(O) - 1, 1))
    for i in range(len(O) - 1):
        mi_s[i][0] = height_node(T, s, O[i + 1]) - constant
    mi_s = mi * mi_s
    return mi_s

def delayCovariance(T, O, sigma2):
    # TODO stop using all_simple_paths (complexity)
    n = len(O)
    delta = np.zeros(shape=(n - 1, n - 1))
    T = T.to_undirected()
    for k in range(n - 1):
        for i in range(n - 1):
            if i == k:
                delta[k][i] = len(list(nx.all_simple_paths(T, O[0], O[k + 1]))[0]) - 1
            else:
                c1 = list(nx.all_simple_paths(T, O[0], O[k + 1]))[0]
                c2 = list(nx.all_simple_paths(T, O[0], O[i + 1]))[0]
                S = [x for x in c1 if x in c2]
                delta[k][i] = len(S) - 1
    delta = delta * (sigma2 ** 2)  # FIXME : square or not ?
    return delta