import sys
import math
import numpy as np

from src.GMLA import gmla
from src.PTVA import ptva
from src.load import load
from src.infect import infect_graph
from src.color_nodes import coloring
from src import accuracy as acc


def main():

    ## Handle inputs
    if len(sys.argv)<3:
        print("Please pass the  algo and dataset name...")
        return
    algo = str(sys.argv[1]).lower()
    title = sys.argv[2]

    ## Load graph
    G, _ = load(title)

    ## Infect graph
    G, arrivalTime, sourceNodes = infect_graph(G, title=title)

    ## Take observers
    k0 = math.ceil(math.sqrt(len(G)))
    np.random.seed(23)
    observers = np.random.choice(len(G),k0, replace=False).tolist()

    ## mean and variance
    t=[]
    for i in observers:
        if(arrivalTime[i]!=-1):
            t.append(arrivalTime[i])
    mn = np.mean(t)
    sigma2 = np.var(t)

    ## assigning time attr to each node.
    for i in range(0, k0):
        G.nodes[observers[i]]['time'] = t[i]

    ## Run algos
    score = []
    if algo == 'ptva':
        score = ptva.PTVA(G, observers, k0, sigma2, mn)
    elif algo == 'gmla':
        score = gmla.GMLA(G, observers, k0, sigma2, mn)
    else:
        print("Error: Enter the correct algo name")
        return
    
    scoreList = [score[i][0] for i in range(5)]
    nodes = [list(a)[0] for a in G.nodes(data=True)]

    coloring(title, G, nodes, scoreList, observers, algo)

    print()
    print(f'Sources : {sourceNodes}')
    print(f'Predicted : {scoreList}')
    print(f'accuracy : {acc.accuracy(sourceNodes,scoreList)} %')

if  __name__ == '__main__':
    main()