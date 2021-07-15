import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep


def infect_graph(g):
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

  # Model Configuration
  cfg = mc.Configuration()
  cfg.add_model_parameter('beta', 0.03)
  cfg.add_model_parameter("fraction_infected", 0.06)
  model.set_initial_status(cfg)

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

  print("Time of diffusion: ")
  print(time_of_diffusion)
  sorted_values = sorted(time_of_diffusion.values()) # Sort the values
  sorted_dict = {}

  for i in sorted_values:
      for k in time_of_diffusion.keys():
          if time_of_diffusion[k] == i:
              sorted_dict[k] = time_of_diffusion[k]
  print("\nSorted Values: ")
  print(sorted_dict)
  return (G, time_of_diffusion)