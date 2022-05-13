import networkx as nx
import pydot
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import *

G = nx.DiGraph()

# хабы, пронумерованные уникальными (в дереве) номерами
and_nodes =[1,7,6,8]
or_nodes =[4]
rw_nodes = [2,3,9,10]
i_nodes = [5,11]

# соединяем их в граф - кого к кому крепить стрелками
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(4, 7)
G.add_edge(4, 6)
G.add_edge(4, 8)
G.add_edge(8, 9)
G.add_edge(8, 10)
G.add_edge(10, 11)

# ОТРИСОВКА --------------------------------------
# стилили рисования разных типов хабов
options_and = {"edgecolors": "tab:gray", "alpha": 0.9, "node_color":"tab:red", "node_shape":'o'}
options_or = {"edgecolors": "skyblue",  "alpha": 0.9, "node_color":"skyblue", "node_shape":'v'}
options_rw = {"edgecolors": "tab:gray",  "alpha": 0.9, "node_color":"white", "node_shape":'s'}
options_i = {"edgecolors": "gray",  "alpha": 0.5, "node_color":"tab:gray", "node_shape":'o', 'linewidths':6}

# рисовка ввиде именно дерева, а не абы как
pos = pydot_layout(G, prog="dot", root=1)

# рисуем вершины
nx.draw_networkx_nodes(G, pos, nodelist=and_nodes, **options_and)
nx.draw_networkx_nodes(G, pos, nodelist=or_nodes, **options_or)
nx.draw_networkx_nodes(G, pos, nodelist=rw_nodes, **options_rw)
nx.draw_networkx_nodes(G, pos, nodelist=i_nodes, **options_i)

# рисуем стрелки
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# на всех хабах нарисуем их номера в дереве(например)
labels = {}
for hub_id in and_nodes:
    labels[hub_id]=hub_id

for hub_id in or_nodes:
    labels[hub_id]=hub_id

for hub_id in rw_nodes:
    labels[hub_id]=hub_id

for hub_id in i_nodes:
    labels[hub_id]=hub_id
nx.draw_networkx_labels(G, pos, labels, font_color="black")

plt.tight_layout()
plt.axis("off")
plt.show()