import pandas as pd
import networkx as nx

def from_pandas_dataframe(df, source, target, edge_attr=None, create_using=None):
    """
    Creats graph using dataframe.
    Parameters:
        df : DataFrame
        source : source column
        target : target column
        edge_attr : edge attributes if any.
    Returns:
        G : Required graph
    """
    g = nx.Graph()
    # Index of source and target
    src_i = df.columns.get_loc(source)
    tar_i = df.columns.get_loc(target)
    if edge_attr:
        # If all additional columns requested, build up a list of tuples
        # [(name, index),...]
        if edge_attr is True:
            # Create a list of all columns indices, ignore nodes
            edge_i = []
            for i, col in enumerate(df.columns):
                if col is not source and col is not target:
                    edge_i.append((col, i))
        # If a list or tuple of name is requested
        elif isinstance(edge_attr, (list, tuple)):
            edge_i = [(i, df.columns.get_loc(i)) for i in edge_attr]
        # If a string or int is passed
        else:
            edge_i = [(edge_attr, df.columns.get_loc(edge_attr)), ]

        # Iteration on values returns the rows as Numpy arrays
        for row in df.values:
            g.add_edge(row[src_i], row[tar_i], {i: row[j] for i, j in edge_i})

    # If no column names are given, then just return the edges.
    else:
        for row in df.values:
            g.add_edge(row[src_i], row[tar_i])
    return g

def make_graph(title):
  """ Read the CSV file
  
  Returns:
  g : Graph
  n : node length
  """ 
  filename = title
  df = pd.read_csv(f'./data/{title}.csv', delimiter=',')
  df = df[["Source", "Target"]].astype(int)
  print(df)
  g = from_pandas_dataframe(df, source='Source', target='Target')
  node_len = len(g.nodes)
  # nx.draw(g,with_labels = True)
  # plt.savefig(filename + "data_GMLA1.png")
  # plt.show()
  return g, node_len