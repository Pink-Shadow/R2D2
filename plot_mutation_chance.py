import copy
import math
import numpy as np
import matplotlib.pyplot as plt 
from operator import index
import time
import random
import itertools as it

class DrawObject:
    def __init__(self, id):
        self.begin = []
        self.end = []

        self.id = id
        self.Gcode = []

    def __repr__(self):
        return f"{self.id}"
        
        
    def get_gcode(self):
        gcode = []

        gcode.append(f"G0 X{self.begin[0]} Y{self.begin[1]}")
        for line in self.Gcode:
            gcode.append(line)

        return gcode
        

def parse_gcode():
    objects = []
    id = 1
    with open(f"gcode.txt", "r") as gcode:
        data = gcode.readlines()
        tmp = DrawObject(id)
        for i, line in enumerate(data):
            line = line.strip()
            if line.startswith('G0'):
                tmp.Gcode.append(line)

                elements = line.split(' ')
                for e in elements:
                    c = e[0]
                    if c == 'X':
                        tmp.begin.append(int(e.strip()[1:]))
                    if c == 'Y':
                        tmp.begin.append(int(e.strip()[1:]))

            elif line.startswith('G1') and (data[i+1].startswith('G0') or (i+1 == len(data)) or data[i+1].startswith('G28')) :
                tmp.Gcode.append(line)

                elements = line.split(' ')
                for e in elements:
                    c = e[0]
                    if c == 'X':
                        tmp.end.append(int(e.strip()[1:]))
                    if c == 'Y':
                        tmp.end.append(int(e.strip()[1:]))
                objects.append(copy.deepcopy(tmp))

                id +=1 
                tmp = DrawObject(id)
                
            else:
                tmp.Gcode.append(line)

    return objects


def write_route_gcode_to_file(route):
    with open(f"route.txt", "w") as gcode:
        for object in route:
            code = object.get_gcode()
            for line in code:
                gcode.write(line + "\n")


##################################################

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def calculate_dist_route(route):
    dist = calculateDistance(0, 0, route[0].begin[0], route[0].begin[1])
    for i in range(len(route)-1):
        dist += calculateDistance(route[i].end[0], route[i].end[1], route[i+1].begin[0], route[i+1].begin[1])
    dist += route[-1].end[0]+route[-1].end[1]

    return dist
    
def calculate_best_route(objects, iterations, mut_chance):
    first_route = copy.deepcopy(objects)
    best_route = first_route
    best_dist = calculate_dist_route(best_route)

    mutation_chance = mut_chance
    improvements = 0
    for i in range(iterations):
        # get longest object distance in route
        longest_dist_step = 0
        longest_index = 0
        longest_object_target = best_route[longest_index]

        second_longest_dist_step = 0
        second_longest_index = 0
        second_longest_object_target = best_route[second_longest_index]
        for i in range(len(best_route)-1):
            dist = calculateDistance(best_route[i].end[0], best_route[i].end[1], best_route[i+1].begin[0], best_route[i+1].begin[1])
            if dist > longest_dist_step:
                longest_dist_step = dist
                longest_index = i+1
                longest_object_target = best_route[i+1]
            elif dist > second_longest_dist_step:
                second_longest_dist_step = dist
                second_longest_index = i+1
                second_longest_object_target = best_route[i+1]
        

        best_route[longest_index], best_route[second_longest_index] = best_route[second_longest_index], best_route[longest_index]

        if random.random() < mutation_chance:
            random_1 = random.choice(range(len(best_route)))
            random_2 = random.choice(range(len(best_route)))
            best_route[random_1], best_route[random_2] = best_route[random_2], best_route[random_1]

        new_dist = calculate_dist_route(best_route)
        if new_dist < best_dist:
            best_dist = new_dist
            best_route = copy.deepcopy(best_route)
            improvements += 1
    return best_route, improvements


if __name__ == "__main__":
    objects = parse_gcode()

    measurements = 30
    data_points = [(i*1/measurements) for i in range(0, measurements+1)]
    iterations = 20000
    improvements = []


    first_route = copy.deepcopy(objects)
    shortest_route = first_route
    shortest_dist = calculate_dist_route(first_route)
    best_mut_chance = data_points[0]

    for i in data_points:
        new_route, improv = calculate_best_route(objects, iterations, i)
        improvements.append(improv)
        dist = calculate_dist_route(new_route)
        if shortest_dist == -1 or dist < shortest_dist:
            print(f"change to: {dist} from {shortest_dist}")
            shortest_route = copy.deepcopy(new_route)
            shortest_dist = dist
            best_mut_chance = i

    plt.plot(data_points, improvements, 'b-')
    plt.show()
    # write_route_gcode_to_file(shortest_route)
    # print(shortest_route)
    # print(f"iterations: {iterations}")