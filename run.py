import sys
import numpy as np
import math

from src.infect import *
from src.load import make_graph
from src.GMLA import algos
from src.color_nodes import coloring
import src.accuracy as acc


def run():
  """
  Main function
  
  Plots 3 graphs :
    1. Original graph
    2. Infected graph
    3. Predicted graph
  """

  if len(sys.argv)<2:
      print("Please pass the dataset name...")
      return

  title = sys.argv[1]
  G, node_len = make_graph(title=title)
  G, time_of_diffusion, source_nodes = infect_graph(G, title=title)
  k0 = math.ceil(math.sqrt(len(G)))
  np.random.seed(23)
  O = np.random.choice(len(G),k0, replace=False).tolist()

  t=[]
  for i in O:
      if(time_of_diffusion[i]!=-1):
          t.append(time_of_diffusion[i])

  print("\nTotal nodes :", node_len)
  print("\nObservers :")
  print(O)
  print("\nTime of diffusion of observers :")
  print(t)

  for a in range(0, k0):
    G.nodes[O[a]]['time'] = t[a]
  mn = np.mean(t)
  sigma2 = np.var(t)

  score = algos.GMLA(G, O, k0, sigma2, mn)
  score_list = [score[i][0] for i in range(5)]
  nodes = [list(a)[0] for a in G.nodes(data=True)]

  coloring(title, G, nodes, score_list, O)

  print()
  print(f'Sources : {source_nodes}')
  print(f'Predicted : {score_list}')
  print(f'accuracy : {acc.accuracy(source_nodes,score_list)} %')
  


if __name__ == '__main__':
    run()