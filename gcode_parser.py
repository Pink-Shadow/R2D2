import copy


class gcode_class:
    def __init__(self):
        self.G: int = 0
        self.X: int = 0
        self.Y: int = 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"G{str(self.G)} X{str(self.X)} Y{str(self.Y)}"


def getStartToEnd(coords):
    coordinates = copy.deepcopy(coords)
    tmp = []
    listWithLines = []
    for x in range(len(coordinates) - 1):
        if coordinates[x + 1].G != 0:
            tmp.append(coordinates[x])
            tmp.append(coordinates[x + 1])
            listWithLines.append(copy.copy(tmp))
            tmp = []
        else:
            coordinates[x].G = 1
    return listWithLines


def parse_gcode(file_name):
    gcode = []
    prev_line = ""
    with open(file_name, "r") as gcode_file:
        data = gcode_file.readlines()
        for line in data:
            if line == prev_line:            
                prev_line = line
                continue
            prev_line = line
            tmp = gcode_class()
            elements = line.split(' ')
            for e in elements:
                c = e[0]
                if c == 'X':
                    tmp.X = int(e.strip()[1:])
                if c == 'Y':
                    tmp.Y = int(e.strip()[1:])
                if c == 'G' and len(elements) > 1:
                    tmp.G = int(e.strip()[1:])
            gcode.append(copy.copy(tmp))
    return copy.deepcopy(gcode)
