import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def load(title):
    df = pd.read_csv(f'./data/{title}.csv').astype(int)
    Graphtype = nx.Graph()
    G = nx.from_pandas_edgelist(df, source='Source',target='Target',create_using=Graphtype)
    nx.draw(G, with_labels=True)
    plt.clf()
    nx.draw(G,with_labels = True)
    plt.savefig(f'./plots/{title}_data.png')

    return G, len(G)