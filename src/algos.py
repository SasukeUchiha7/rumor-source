## packages
import networkx as nx
import numpy as np

from src.helpers import *


def GMLA(G,O,k0, sigma2, mn):
  """Main Function

  Parameters:
    G : Graph
    O : Observers node list
    k0 : Constant k0
    simga2 : Sigma^2 (var) of diffudion time
    mn :  Mean of diffusion time
  Returns:
    sortedScore (list[tuple]) : Sorted scores of node based on the algo. 
  """
  ##sort obs
  ## filtering k0 nos from O.
  nearestObs = O[0:k0]
  ## selecting first_observer
  first_obv = O[0]

  ##computing obs delay wrt O[0].
  d = observedDelay(G,nearestObs)

  S = {}
  v = [first_obv,0]
  maxScore = 0

  while v[1] >= maxScore:
    Tv = {}
    for n in list(G.neighbors(v[0])):
      if n not in S:
        diffusionTree = nx.bfs_tree(G, source=n)
        mu_n = deterministicDelay(diffusionTree, n, O, mn)
        delta_n = delayCovariance(diffusionTree, O, sigma2)
        inverse = np.linalg.inv(delta_n)
        score = (np.exp(-.5 * np.dot(np.dot((d - mu_n).T, inverse), (d - mu_n)))) / (np.sqrt(abs(np.linalg.det(delta_n))))
        print(f" for {n} neighbor of {v[0]}, score: {score}")
        Tv[n] = score[0][0]
    if len(Tv) !=0:
      sortedTv = sorted(Tv.items(), key=lambda x:x[1], reverse=True)
      print(f"Dont know what this is for {v[0]}  --> {v[1]}: {sortedTv}")
      v = [(sortedTv)[0][0],(sortedTv)[0][1]]
      S.update(Tv)
      maxScore = v[1]
    else:
      break

  sortedScore = sorted(S.items(), key=lambda x: x[1], reverse=True)

  print("The rumor scores order: ")
  for i in range(len(sortedScore)):
    print(f'{sortedScore[i][0]} : {sortedScore[i][1]}')

  return sortedScore

