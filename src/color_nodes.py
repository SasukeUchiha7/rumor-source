import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D

_legends = [Line2D([0], [0], marker='o', color='w', label='Source', markerfacecolor='r', markersize=15),
Line2D([0], [0], marker='o', color='w', label='Observers', markerfacecolor='g', markersize=15),
Line2D([0], [0], marker='o', color='w', label='Others', markerfacecolor='b', markersize=15),]

node_color = []

def coloring(title, G, nodes, score_list, O, algo):
    for i in nodes:
        if i in score_list:
            node_color.append('red')
        elif i in O:
            node_color.append('green')
        else:
            node_color.append('blue')

    plt.clf()
    nx.draw(G,with_labels = True, node_size=200, node_color=node_color)
    plt.legend(_legends, ['Source','Observers','Others'], loc="upper right")
    plt.savefig(f'./plots/{title}_{algo}.png')