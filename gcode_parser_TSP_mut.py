import copy
import math
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
    

if __name__ == "__main__":
    objects = parse_gcode()

    iterations = 1
    first_route = copy.deepcopy(objects)
    shortest_route = first_route
    shortest_dist = calculate_dist_route(first_route)

    # the chance of a random mutation happening per iteration
    mutation_chance = 0.1

    current_time = time.perf_counter()
    while time.perf_counter() - current_time < 60:
        # indexes = random.sample(range(len(objects)), mutations*2)

        # get longest object distance in route
        longest_dist_step = 0
        longest_index = 0
        longest_object_target = objects[longest_index]

        second_longest_dist_step = 0
        second_longest_index = 0
        second_longest_object_target = objects[second_longest_index]
        for i in range(len(objects)-1):
            dist = calculateDistance(objects[i].end[0], objects[i].end[1], objects[i+1].begin[0], objects[i+1].begin[1])
            if dist > longest_dist_step:
                longest_dist_step = dist
                longest_index = i+1
                longest_object_target = objects[i+1]
            elif dist > second_longest_dist_step:
                second_longest_dist_step = dist
                second_longest_index = i+1
                second_longest_object_target = objects[i+1]
        

        objects[longest_index], objects[second_longest_index] = objects[second_longest_index], objects[longest_index]

        if random.random() < mutation_chance:
            random_1 = random.choice(range(len(objects)))
            random_2 = random.choice(range(len(objects)))
            objects[random_1], objects[random_2] = objects[random_2], objects[random_1]

        dist = calculate_dist_route(objects)
        if shortest_dist == -1 or dist < shortest_dist:
            print(f"change to: {dist} from {shortest_dist}")
            shortest_route = copy.deepcopy(objects)
            shortest_dist = dist
        iterations += 1

    write_route_gcode_to_file(shortest_route)
    print(shortest_route)
    print(f"iterations: {iterations}")