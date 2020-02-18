import networkx as nx
import matplotlib.pyplot as plt

# loading the college football network
G = nx.read_gml('football.gml')

# drawing the graph  --- Kamada-Kawai layout
plt.figure(figsize=[12,12])
pos = nx.kamada_kawai_layout(G, weight=None) # positions for all nodes
# extracting conference information
conf = []
for i,d in G.nodes(data=True):
    conf.append(d['value'])
# drawing nodes, different conferences in different colors
for iConf in range(12):
    nx.draw_networkx_nodes(G, pos,
                           cmap=plt.cm.plasma, node_color=conf)
nx.draw_networkx_edges(G, pos, edge_color='lightblue')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='DarkGreen')
plt.axis('off')
plt.title('College football network')
plt.show()