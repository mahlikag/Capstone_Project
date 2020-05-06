## Networkx
# The following is a program designed to create a graph based on some city clearance rates
# The program imports the data, assigns the information to the nodes as attributes
# And then draws the graph based on a defined function name 'euclideanDistance'
import math as m

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# This command reads in the cleaned excel sheet
df = pd.read_excel('testing.xlsx')


# The following commands separates the imported data frame into columns
state = df['State']
city = df['City']
population = df['Total.Population']
A_clearance = df['Aggravated.Assault.Clearance.Rate']
R_clearance = df['Robbery.Clearance.Rate']
M_clearance = df['Murder.Nonnegligent.Manslaughter.Clearance.Rate']

# The a series of blank lists are created for future use
states = []
cities = []
populations = []
A_clearance_rate = []
M_clearance_rate = []
R_clearance_rate = []


# The following set of for loops take the columns from the data frame and then stores
# the information in a set of lists. Lists are easier to add as attributes
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


# Now that the lists are created, a NetworkX graph using the command nx.Graph() is used to create a blank graph/network
G = nx.Graph()

# One hundred nodes are created to represent the 100 cities
for x in range(0, 100):
    G.add_node(x)

# The following adds a 'state' attribute to each of the nodes based on the information on the excel sheet
i = 0
for x in range(0, 100):
    G.nodes[i]['state'] = states[x]
    i = i + 1

# The following adds a 'city' attribute to each of the nodes based on the information on the excel sheet
i = 0
for x in range(0, 100):
    G.nodes[i]['city'] = cities[x]
    i = i + 1

# The following adds a 'population' attribute to each of the nodes based on the information on the excel sheet
i = 0
for x in range(0, 100):
    G.nodes[i]['population'] = populations[x]
    i = i + 1

# The following adds the 'aggravated assault clearance rate' attribute to each of the nodes
# based on the information on the excel sheet
i = 0
for x in range(0, 100):
    G.nodes[i]['A_CR'] = A_clearance_rate[x]
    i = i + 1

# The following adds the 'murder clearance rate' attribute to each of the nodes
# based on the information on the excel sheet
i = 0
for x in range(0, 100):
    G.nodes[i]['M_CR'] = M_clearance_rate[x]
    i = i + 1

# The following adds the 'robbery clearance rate' attribute to each of the nodes
# based on the information on the excel sheet
i = 0
for x in range(0, 100):
    G.nodes[i]['R_CR'] = R_clearance_rate[x]
    i = i + 1


##
# This function calculates the euclidean distance between two given cities
# This distance is based on their clearance rate values for the three different crimes
# @a The first city of observation in the distance calculation
# @b The second city of observation in the distance calculation
# return The return of the function is the calculated distance between the cities
def euclideanDistance(a, b):
    diff1 = float(G.nodes[a]['A_CR']) - float(G.nodes[b]['A_CR'])
    diff2 = float(G.nodes[a]['M_CR']) - float(G.nodes[b]['M_CR'])
    diff3 = float(G.nodes[a]['R_CR']) - float(G.nodes[b]['R_CR'])
    distance = m.sqrt((diff1 ** 2) + (diff2 ** 2) + (diff3 ** 2))
    return distance


# This command creates a dictionary for the positions of the nodes that will be later given
positions = {}

# These two files store the latitude and longitude of every single city in the network
x = open('X_Coordinates.txt', 'r')
y = open('Y_Coordinates.txt', 'r')

# Since the text file might have extra lines and spaces, two empty lists are created
x_coords = []
y_coords = []

# These lists are then appended with the information in the previous text files to produce
# Two separate lists of the x and y coordinates (from the city geographic longitude and latitude)
for a in x:
    x_coords.append(a.strip())
for a in y:
    y_coords.append(a.strip())


# The cooridnates are converted into floats instead of strings
# The x coordinates are multiplied by -1 because America is on the west side of the world
# In terms of longitude west is negative and east is positive
i = 0
for x in range(0, 100):
    positions[i] = [-float(x_coords[x]), float(y_coords[x])]
    i = i + 1


##
# To create the colors, this programs goes with a grouping approach
# The colors are based of a high, low, and medium rate
# High meaning very similar so the distance is 3 or less
# Medium meaning okay similarity so the distance is between 3 and 5
# Low meaning somewhat similar so the distance id between 5 and 10
# And nodes with a distance between them that is more than 10 are considered "far"

##
# To change the colors of the nodes in NetworkX, you have to create a list the same length of the
# of the number of nodes. An empty list if created
# All of the nodes are initialized to a black color
color_map = ['black'] * 100


##
# If the distance is ten or less, and edge between the nodes is formed and the color is set to yellow
# But if the distance is also lower than 5, the color is set to orange
# But if the distance is also lower than 3, the color is set to red
# This is done for every combination of nodes possible

for a in range(0, 99):
    for b in range(a + 1, 100):
        if euclideanDistance(a, b) <= 10:
            G.add_edge(a, b)
            color_map[a] = 'yellow'
            color_map[b] = 'yellow'
for a in range(0, 99):
    for b in range(a + 1, 100):
        if euclideanDistance(a, b) <= 5:
            color_map[a] = 'orange'
            color_map[b] = 'orange'

for a in range(0, 99):
    for b in range(a + 1, 100):
        if euclideanDistance(a, b) <= 3:
            color_map[a] = 'red'
            color_map[b] = 'red'

##
# To color the edges, again, a list of the chosen colors has to be created for matplotlib
low_edge_list = []
med_edge_list = []
high_edge_list = []

##
# G.edges displays every single edge formed between nodes. So if there is an edge between nodes 1 and 34
# G.edges will have a value in its list that looks like (1, 34)
# With that im mind, this for loops iterates through all the already formed edges
# And it puts the edges in a group based on the conditions below
# In the example with (1, 34), x[0] would equal 1 and x[1] would equal 34
# The for loop with check its distance and add that edge, (1,34), to one of the groups
# Again, this is done for every pair of edges
for x in G.edges:
    if euclideanDistance(x[0], x[1]) <= 3:
        high_edge_list.append(x)
    if 3 < euclideanDistance(x[0], x[1]) <= 5:
        med_edge_list.append(x)
    if 5 < euclideanDistance(x[0], x[1]) <= 10:
        low_edge_list.append(x)


# The labels for the nodes in the graph will be the city names
labels = {i: cities[i] for i in range(0, len(cities))}


##
# The following utilizes matplotlib to actually graph the network
# The labels again will be the city names
# The positions will be based on the position dictionary created
# The node color is set to the color map previously created
# The edges are initialized to a gray color
plt.figure(figsize=(15, 15))
nx.draw_networkx(G, positions, node_size=200, node_color=color_map, labels=labels, font_size=8, font_color='gray')

##
# The creates the edge specifications
# The node colors will be based on the color map again but given a particular edge list, the edge color
# is specified here
# Red for the high group, orange for the medium group, and light gray for the low group
# Yellow wasn't used for the edges like it was used for the nodes because yellow lines are harder to see
# And can look very similar to the orange lines
nx.draw_networkx_edges(G, positions, node_size=200, node_color=color_map, font_color='w', edgelist=high_edge_list,
                       edge_color='red')
nx.draw_networkx_edges(G, positions, node_size=200, node_color=color_map, font_color='w', edgelist=med_edge_list,
                       edge_color='orange')
nx.draw_networkx_edges(G, positions, node_size=200, node_color=color_map, font_color='w', edgelist=low_edge_list,
                       edge_color='lightgrey')

# This command will display the plot/graph
plt.show()

# This new variable 'spring' will be our new positioning variable instead of
# the longitude and latitude
spring = nx.spring_layout(G)

##
# This new plot keeps everything exactly the same
# However, instead of using positions, the variable spring will be used
# That will position the nodes based on the spring layout calculations from
# The built-in NetworkX function
plt.figure(figsize=(15, 15))
nx.draw_networkx(G, spring, node_size=200, node_color=color_map, with_labels=False)
nx.draw_networkx_edges(G, spring, node_size=200, node_color=color_map, font_color='w', edgelist=high_edge_list,
                       edge_color='red')
nx.draw_networkx_edges(G, spring, node_size=200, node_color=color_map, font_color='w', edgelist=med_edge_list,
                       edge_color='orange')
nx.draw_networkx_edges(G, spring, node_size=200, node_color=color_map, font_color='w', edgelist=low_edge_list,
                       edge_color='lightgrey')
nx.draw_networkx_labels(G, spring, labels, font_size=8, font_color='gray')
plt.show()


##
# In addition to the graphs, NetworkX also allows us to see the communities
# To use this import communities
from networkx.algorithms import community


##
# Once the communities are generated, print the number of communities
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
# next_level_communities = next(communities_generator)
print("The number of communities is", len(top_level_communities))

# And print the actual list of the communities
print()
print("The list of communities is: ")
for x in top_level_communities:
    print(x)

