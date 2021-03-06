## packages
from typing import List
import networkx as nx
import numpy as np

from src.GMLA.helpers import *


def GMLA(G,O,k0, sigma2, mn):
  """Main Function for GMLA

  Parameters:
    G : Graph
    O : Observers node list
    k0 : Constant k0
    simga2 : Sigma^2 (var) of diffusion time
    mn :  Mean of diffusion time
  Returns:
    sortedLikelihood (list[tuple]) : Sorted likelihood of node based on the algo. 
  """
  
  ## filtering k0 nos from O.
  nearestObs = O[0:k0]
  
  ## selecting first_observer
  first_obv = nearestObs[0]

  ##computing obs delay wrt O[0].
  d = observedDelay(G,nearestObs)
  
  ## score set
  S = {}

  ## iterator
  v = [first_obv,0]

  maxLikelihood = 0

  while v[1] >= maxLikelihood:
    Tv = {}
    for n in list(G.neighbors(v[0])):
      if n not in S:
        diffusionTree = nx.bfs_tree(G, source=n)
        mu_n = mu(diffusionTree, n, O, mn)
        delta_n = covariance(diffusionTree, O, sigma2)
        likelihood = (np.exp(-0.5 * np.dot(np.dot((d - mu_n).T, np.linalg.inv(delta_n)), (d - mu_n)))) / (np.sqrt(abs(np.linalg.det(delta_n))))
        # print(f" for {n} neighbor of {v[0]}, likelihood: {likelihood}")
        Tv[n] = likelihood[0][0]
    if len(Tv) !=0:
      sortedTv = sorted(Tv.items(), key=lambda x:x[1], reverse=True)
      v = [(sortedTv)[0][0],(sortedTv)[0][1]]
      S.update(Tv)
      maxLikelihood = v[1]
    else:
      break

  sortedLikelihood = sorted(S.items(), key=lambda x: x[1], reverse=True)

  print("\nLikelihood order----------- ")
  for i in range(len(sortedLikelihood)):
    print(f'{sortedLikelihood[i][0]} : {sortedLikelihood[i][1]}')

  return sortedLikelihood

