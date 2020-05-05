##
#efsvnsrjnsr
#svsdndfbcdb
#svsrbdtbrsvse

import networkx as nx
import matplotlib.pyplot as plt
import math as m
import xlrd
import pandas as pd

df = pd.read_excel('testing.xlsx')

state = df['State']
city = df['City']
population = df['Total.Population']
A_clearance = df['Aggravated.Assault.Clearance.Rate']
R_clearance = df['Robbery.Clearance.Rate']
M_clearance = df['Murder.Nonnegligent.Manslaughter.Clearance.Rate']
states = []
cities = []
populations = []
A_clearance_rate = []
M_clearance_rate = []
R_clearance_rate = []

for x in state:
    states.append(x)

for x in city:
    cities.append(x)

for x in population:
    populations.append(x)

for x in A_clearance:
    A_clearance_rate.append(x)

for x in M_clearance:
    M_clearance_rate.append(x)

for x in R_clearance:
    R_clearance_rate.append(x)

G = nx.Graph()
for x in range(0, 100):
    G.add_node(x)

i = 0
for x in range(0, 100):
    G.nodes[i]['state'] = states[x]
    i = i + 1

i = 0
for x in range(0, 100):
    G.nodes[i]['city'] = cities[x]
    i = i + 1

i = 0
for x in range(0, 100):
    G.nodes[i]['population'] = populations[x]
    i = i + 1

i = 0
for x in range(0, 100):
    G.nodes[i]['A_CR'] = A_clearance_rate[x]
    i = i + 1

i = 0
for x in range(0, 100):
    G.nodes[i]['M_CR'] = M_clearance_rate[x]
    i = i + 1

i = 0
for x in range(0, 100):
    G.nodes[i]['R_CR'] = R_clearance_rate[x]
    i = i + 1


def euclideanDistance(a, b):
    diff1 = float(G.nodes[a]['A_CR']) - float(G.nodes[b]['A_CR'])
    diff2 = float(G.nodes[a]['M_CR']) - float(G.nodes[b]['M_CR'])
    diff3 = float(G.nodes[a]['R_CR']) - float(G.nodes[b]['R_CR'])
    distance = m.sqrt((diff1 ** 2) + (diff2 ** 2) + (diff3 ** 2))
    return distance


positions = {}
x = open('X_Coordinates.txt', 'r')
y = open('Y_Coordinates.txt', 'r')

x_coords = []
y_coords = []

for a in x:
    x_coords.append(a.strip())
for a in y:
    y_coords.append(a.strip())

i = 0
for x in range(0, 100):
    positions[i] = [-float(x_coords[x]), float(y_coords[x])]
    i = i + 1

color_map = []
for x in range(0, 100):
    color_map.append('black')
for a in range(0, 99):
    for b in range(a + 1, 100):
        if euclideanDistance(a, b) <= 10:
            G.add_edge(a, b)
            color_map[a] = 'yellow'
            color_map[b] = 'yellow'
for a in range(0, 99):
    for b in range(a + 1, 100):
        if euclideanDistance(a, b) <= 5:
            G.add_edge(a, b)
            color_map[a] = 'orange'
            color_map[b] = 'orange'

for a in range(0, 99):
    for b in range(a + 1, 100):
        if euclideanDistance(a, b) <= 3:
            G.add_edge(a, b)
            color_map[a] = 'red'
            color_map[b] = 'red'

low_edge_list = []
med_edge_list = []
high_edge_list = []

for x in G.edges:
    if euclideanDistance(x[0], x[1]) <= 3:
        high_edge_list.append(x)
    if 3 < euclideanDistance(x[0], x[1]) <= 5:
        med_edge_list.append(x)
    if 5 < euclideanDistance(x[0], x[1]) <= 10:
        low_edge_list.append(x)

labels = {i: cities[i] for i in range(0, len(cities))}

plt.figure(figsize=(15, 15))
nx.draw_networkx(G, positions, node_size=200, node_color=color_map, labels=labels, font_size=8, font_color='gray')
nx.draw_networkx_edges(G, positions, node_size=200, node_color=color_map, font_color='w', edgelist=high_edge_list,
                       edge_color='red')
nx.draw_networkx_edges(G, positions, node_size=200, node_color=color_map, font_color='w', edgelist=med_edge_list,
                       edge_color='orange')
nx.draw_networkx_edges(G, positions, node_size=200, node_color=color_map, font_color='w', edgelist=low_edge_list,
                       edge_color='lightgrey')
plt.show()

pos = nx.spring_layout(G)
plt.figure(figsize=(15, 15))
nx.draw_networkx(G, pos, node_size=200, node_color=color_map, with_labels=False)
nx.draw_networkx_edges(G, pos, node_size=200, node_color=color_map, font_color='w', edgelist=high_edge_list,
                       edge_color='red')
nx.draw_networkx_edges(G, pos, node_size=200, node_color=color_map, font_color='w', edgelist=med_edge_list,
                       edge_color='orange')
nx.draw_networkx_edges(G, pos, node_size=200, node_color=color_map, font_color='w', edgelist=low_edge_list,
                       edge_color='lightgrey')
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='gray')
plt.show()

from networkx.algorithms import community

communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
# next_level_communities = next(communities_generator)
print("The number of communities is", len(top_level_communities))

print()
print("The list of communities is: ")
print(top_level_communities)

