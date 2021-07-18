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
  timeOfDiffusions=[]
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

  #Mapping diffusion_time_to_each_node
  time_of_diffusion={}
  for i in range(1,len(G)):
      time_of_diffusion[i]=-1
  for i in iterations:
      for j in i['status']:
          if(i['status'][j]==1):
              time_of_diffusion[j]=i['iteration']
  timeOfDiffusions.append(len(time_of_diffusion))
  
  nodeColor = []
  source_nodes = []
  for i in G.nodes():
    if iterations[0]["status"][i]==1:
      nodeColor.append('red')
      source_nodes.append(i)
    else:
      nodeColor.append('blue')

  # print("Time of diffusion: ")
  # print(time_of_diffusion)
  sorted_values = sorted(time_of_diffusion.values()) # Sort the values
  sorted_dict = {}

  for i in sorted_values:
      for k in time_of_diffusion.keys():
          if time_of_diffusion[k] == i:
              sorted_dict[k] = time_of_diffusion[k]
  # print("\nSorted Values of diffusion time: ")
  # print(sorted_dict)
  plt.clf()
  nx.draw(G, node_color=nodeColor, with_labels=True)
  plt.title('Intial Phase')
  plt.savefig(f'./plots/{title}_Initial-infect.png')

  return (G, time_of_diffusion, source_nodes)