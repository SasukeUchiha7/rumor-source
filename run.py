import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx

from src.infect import *
from src.load import make_graph
from src import algos

def run():
  G, node_len = make_graph(title='dolphin')
  G, time_of_diffusion = infect_graph(G)
  k0 = math.ceil(math.sqrt(len(G)))
  np.random.seed(54)
  O = np.random.choice(len(G),k0, replace=False).tolist()

  t=[]
  for i in O:
      if(time_of_diffusion[i]!=-1):
          t.append(time_of_diffusion[i])
  print(O)
  print(t)
  for a in range(0, k0):
    G.nodes[O[a]]['time'] = t[a]
  mn = np.mean(t)
  sigma2 = np.var(t)

  score = algos.GMLA(G, O, k0, sigma2, mn)
  score = [list(a)[0] for a in G.nodes(data=True)]
  print(score)

  
  node_color = []
  count = 0
  score_list = score[0:5]
  for i in range(1, node_len + 1):
      if i in O:
          node_color.append('green')
      elif i in score_list:
          node_color.append('red')
      elif 5 == 5:
          count = count + 1
          node_color.append('blue')
  nx.draw(G,with_labels = True, node_size=200, node_color=node_color,
          alpha=1, linewidths=0.5, width=0.5, edge_color='black')
  # plt.savefig(filename+"GMLA.png")
  # plt.show()


if __name__ == '__main__':
    run()