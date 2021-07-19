from matplotlib import pyplot as plt
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
import networkx as nx


def infect_graph(g, title):
  """
  Function to infect the graph using SI model.
  Parameters:
    g: Graph 
  Returns:
    G : Infected graph
    t : Time of diffusion of each node
  """
  G=g
  # Model selection - diffusion time
  model = ep.SIModel(G)
  nos = 1/len(G)
  # Model Configuration
  config = mc.Configuration()
  config.add_model_parameter('beta', 0.03)
  config.add_model_parameter("fraction_infected", 0.05)
  model.set_initial_status(config)

  # Simulation execution
  iterations = model.iteration_bunch(200)

  diffusionTime={}
  for i in range(1,len(G)):
      diffusionTime[i]=-1

  for i in iterations:
      for j in i['status']:
          if(i['status'][j]==1):
              diffusionTime[j]=i['iteration']
  
  nodeColor = []
  source_nodes = []
  for i in G.nodes():
    if iterations[0]["status"][i]==1:
      nodeColor.append('red')
      source_nodes.append(i)
    else:
      nodeColor.append('blue')

  sorted_values = sorted(diffusionTime.values()) # Sort the values
  sorted_dict = {}

  for i in sorted_values:
      for k in diffusionTime.keys():
          if diffusionTime[k] == i:
              sorted_dict[k] = diffusionTime[k]

  plt.clf()
  nx.draw(G, node_color=nodeColor, with_labels=True)
  plt.title('Intial Phase')
  plt.savefig(f'./plots/{title}_Initial-infect.png')
  plt.clf()
  nx.draw(G, node_color=list(x for i,x in diffusionTime.items()),cmap=plt.cm.Reds, with_labels=True)
  plt.title('Final Phase')
  plt.savefig(f'./plots/{title}_Final-infect.png')

  return (G, sorted_dict, source_nodes)