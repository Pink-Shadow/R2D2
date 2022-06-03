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
    tmp = []
    listWithLines = []
    for x in range(len(coords) - 1):
        if coords[x + 1].G != 0:
            tmp.append(coords[x])
            tmp.append(coords[x + 1])
            listWithLines.append(copy.copy(tmp))
            tmp = []
    return listWithLines


def parse_gcode():
    coords = []
    with open(f"gcode.txt", "r") as gcode:
        data = gcode.readlines()
        for line in data:
            # if not line.startswith("G0"):
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
            coords.append(copy.copy(tmp))
    return coords



if __name__ == "__main__":
    coords = parse_gcode()
    coords = getStartToEnd(coords)

    for x in coords:
        print(x)