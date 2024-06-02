import math
import random
import stranding
import classes
import csv
import pickle
import matplotlib.pyplot as plt
import array

###############
# Constants
init_radius = 5
cluster_size = 1500
###############

def init_cluster():
    _cluster = [(0, 0)]
    return _cluster

def add_cluster_neighbours(_neighbours, _new_element):
    #print(_new_element.x, _new_element.y)
    _neighbours.add((_new_element.x + 1, _new_element.y))
    _neighbours.add((_new_element.x - 1, _new_element.y))
    _neighbours.add((_new_element.x, _new_element.y + 1))
    _neighbours.add((_new_element.x, _new_element.y - 1))
    _neighbours.add((_new_element.x + 1, _new_element.y + 1))
    _neighbours.add((_new_element.x + 1, _new_element.y - 1))
    _neighbours.add((_new_element.x - 1, _new_element.y + 1))
    _neighbours.add((_new_element.x - 1, _new_element.y - 1))
    return _neighbours

def new_radius(_new_element, _radius):
    _new_radius = init_radius + round(math.sqrt(_new_element.x*_new_element.x + _new_element.y*_new_element.y))
    if _new_radius > _radius:
        return _new_radius
    else:
        return _radius

cluster = init_cluster()
new_element = classes.Element(0, 0)
neighbours = {(0, 0)}
neighbours = add_cluster_neighbours(neighbours, new_element)
#print(neighbours)
radius = init_radius

for elements in range(1, cluster_size):
    stranger_coords = stranding.stranger_spawn(radius)
    #print("init X = ", stranger_coords.x, ", init Y = ", stranger_coords.y)
    new_element = stranding.stranding(stranger_coords, neighbours)
    cluster.append((new_element.x, new_element.y))
    neighbours = add_cluster_neighbours(neighbours, new_element)
    radius = new_radius(new_element, radius)

with open('cluster.txt', 'w') as file:
    for element in cluster:
        file.write(str(element[0]))
        file.write(", ")
        file.write(str(element[1]))
        file.write("\n")

xpoints = array.array('i', [])
ypoints = array.array('i', [])

for element in cluster:
    xpoints.append(element[0])
    ypoints.append(element[1])

plt.plot(xpoints, ypoints, 'o')
plt.show()
