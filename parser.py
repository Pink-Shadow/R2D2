import copy
import math
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
        gcode.append(f"G0 {self.Gcode[0][self.Gcode[0].index('X'):]}")
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

            elif line.startswith('G1') and data[i+1].startswith('G0'):
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

if __name__ == "__main__":
    objects = parse_gcode()
    routes = list(it.permutations(objects)) 
    
    shortest_route = None
    shortest_dist = -1
    for route in routes:    # [1, 2, 0, 7, 8]
        dist = calculateDistance(0, 0, route[0].begin[0], route[0].begin[1])
        for i in range(len(route)-1):
            dist += calculateDistance(route[i].end[0], route[i].end[1], route[i+1].begin[0], route[i+1].begin[1])
        dist += route[-1].end[0]+route[-1].end[1]
        if shortest_dist == -1 or dist < shortest_dist:
            shortest_route = route
            shortest_dist = dist

    print(f"Shortest route: {shortest_route}\nShortest distance: {shortest_dist}")
    write_route_gcode_to_file(shortest_route)