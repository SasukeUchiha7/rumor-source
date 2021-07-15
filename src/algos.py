## packages
import networkx as nx
import numpy as np

from helpers import *


def GMLA(G,O,k0, sigma2, mn):
  """Main Function

  Parameters:
    a : 
    b : 
  Returns:
    c : 
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
        print("score: ", score)
        Tv[n] = score[0][0]
    if len(Tv) !=0:
      print("type of score: ",type(score))
      sortedTv = sorted(Tv.items(), key=lambda x:x[1], reverse=True)
      print(sortedTv)
      v = [list(sortedTv)[0],sortedTv[list(sortedTv)[0]]]
      S.update(Tv)
      maxScore = v[1]
    else:
      break

  sortedScore = sorted(S.items(), key=lambda x: x[1], reverse=True)

  print("The rumor scores order: ")
  for k, v in sortedScore.items():
    print(f'{k} : {v}')

  return sortedScore

