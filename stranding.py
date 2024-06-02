import numpy as np
import math
import random
import classes

# Spawn a stranding particle near the cluster
def stranger_spawn(_radius):
    fi = random.random() * 2 * math.pi  # значение от 0.0 до 2 Пи
    x_stranger = _radius * math.cos(fi)
    y_stranger = _radius * math.sin(fi)
    _stranger_coords = classes.Element(round(x_stranger), round(y_stranger))
    return _stranger_coords

# Shift the particle one cell randomly
def make_step(_stranger_coords):

    x_tuple = (-1, 0 , 1)
    x_shift = random.choice(x_tuple)
    new_x = _stranger_coords.x + x_shift

    if x_shift != 0:
        y_tuple = (-1, 0 , 1)
    else:
        y_tuple = (-1, 1)
    y_shift = random.choice(y_tuple)
    new_y = _stranger_coords.y + y_shift

    new_coords = classes.Element(new_x, new_y)

    return new_coords 

# The particle strands until touch the cluster
def stranding(_stranger_coords, _neighbours):

    ###############
    # Constants
    max_steps = 500
    max_distance = 100
    ###############

    start_coords = _stranger_coords
    should_restart = True
    while should_restart:
        should_restart = False
        for i in range(1, max_steps):

            _stranger_coords = make_step(_stranger_coords)

            if (_stranger_coords.x, _stranger_coords.y) in _neighbours:
                _new_element = classes.Element(_stranger_coords.x, _stranger_coords.y)
                #print("Stick!")
                return _new_element
                break

            if abs(_stranger_coords.x) > max_distance or abs(_stranger_coords.y) > max_distance:
                #print("Gone!")
                _stranger_coords = start_coords
                should_restart = True
                break

            if i == max_steps - 1:
                #print("Max steps received")
                should_restart = True
