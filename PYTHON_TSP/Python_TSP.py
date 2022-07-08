import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing
import copy
import math
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
        for line in self.Gcode:
            if (len(gcode) == 0) or (line != gcode[-1]):
                gcode.append(line)
        return gcode
        
def parse_gcode(filename):
    objects = []
    id = 1
    tmp = DrawObject(0)
    tmp.begin = [30000, 25000]
    tmp.end = [30000, 25000]
    objects.append(copy.deepcopy(tmp))
    with open(filename, "r") as gcode:
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

def write_route_gcode_to_file(objects, route, filename):
    with open(filename, "w") as gcode:
        for index in route:
            code = objects[index].get_gcode()
            for line in code:
                gcode.write(line + "\n")
        gcode.write("G28\n")
# ##################################################

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

# def calculate_dist_route(route):
    # dist = calculateDistance(0, 0, route[0].begin[0], route[0].begin[1])
    # for i in range(len(route)-1):
    #     dist += calculateDistance(route[i].end[0], route[i].end[1], route[i+1].begin[0], route[i+1].begin[1])
    # dist += route[-1].end[0]+route[-1].end[1]

    # return dist
    

def calculate_matrix(objects):
    matrix = np.zeros((len(objects), len(objects)), dtype=int)
    for index in range(len(objects)):
        for index2 in range(len(objects)):
            if index == index2:
                matrix[index][index2]=0
            else:
                matrix[index][index2]=calculateDistance(objects[index].end[0], objects[index].end[1], objects[index2].begin[0], objects[index2].begin[1])    
    return matrix



if __name__ == "__main__":
    filename_tijd =[["aston.txt", 1.4842777013778687],
                    ["cat.txt", 10.325533413887024],
                    ["dog.txt", 18.796085953712463],
                    ["elephant.txt", 42.47500519752502],
                    ["f1.txt", 7.056083798408508],
                    ["ferrari.txt", 2.6067909240722655],
                    ["lambo.txt", 2.1178187847137453],
                    ["leeuw.txt", 50.69488701820374],
                    ["mondriaan_1.txt", 0.031006360054016115],
                    ["mondriaan_2.txt", 2.7649765253067016],
                    ["mondriaan_3.txt", 3.498494338989258],
                    ["mondriaan_4.txt", 44.46061313152313],
                    ["mondriaan_5.txt", 14.679688549041748],
                    ["pauw.txt", 144.00858836174012],
                    ["pug.txt", 34.56406393051147]]
    for file in filename_tijd:
        objects = parse_gcode("../original/" + file[0])
        objects_copy = copy.deepcopy(objects)
        distance_matrix = calculate_matrix(objects_copy)
        with open("objects.txt", "a") as log:
            log.write(f"{file[0]} has {len(objects)} objects\n")
            print(f"{file[0]} has {len(objects)} objects\n")
        for run in range(20):
            permutation, distance = solve_tsp_simulated_annealing(distance_matrix, max_processing_time=file[1])
            print("permutation: ", permutation)
            print("distance: ", distance)
            write_route_gcode_to_file(objects, permutation, f"{run}_{file[0]}")



            