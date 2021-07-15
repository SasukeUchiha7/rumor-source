import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D

from src.infect import *
from src.load import make_graph
from src import algos

_legends = [Line2D([0], [0], marker='o', color='w', label='Source', markerfacecolor='r', markersize=15),
                Line2D([0], [0], marker='o', color='w', label='Observers', markerfacecolor='g', markersize=15),
                Line2D([0], [0], marker='o', color='w', label='Others', markerfacecolor='b', markersize=15),]

def run():
  title ="football"
  G, node_len = make_graph(title=title)
  G, time_of_diffusion = infect_graph(G, title=title)
  k0 = math.ceil(math.sqrt(len(G)))
  np.random.seed(54)
  O = np.random.choice(len(G),k0, replace=False).tolist()

  t=[]
  for i in O:
      if(time_of_diffusion[i]!=-1):
          t.append(time_of_diffusion[i])
  print("Observers :-----------------")
  print(O)
  print("Time of diffusion of observers:----------------")
  print(t)
  for a in range(0, k0):
    G.nodes[O[a]]['time'] = t[a]
  mn = np.mean(t)
  sigma2 = np.var(t)

  score = algos.GMLA(G, O, k0, sigma2, mn)
  nodes = [list(a)[0] for a in G.nodes(data=True)]
  print("Nodes ----------------------------")
  print(nodes)

  
  node_color = []
  score_list = [score[i][0] for i in range(5)]
  for i in nodes:
      if i in score_list:
          node_color.append('red')
      elif i in O:
          node_color.append('green')
      else:
          node_color.append('blue')
  plt.clf()
  nx.draw(G,with_labels = True, node_size=200, node_color=node_color, alpha=1, linewidths=0.5, width=0.5, edge_color='black')
  plt.legend(_legends, ['Source','Observers','Others'], loc="upper right")
  plt.savefig(f'./plots/{title}_GMLA.png')


if __name__ == '__main__':
    run()