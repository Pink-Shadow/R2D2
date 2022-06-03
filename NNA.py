import math
from gcode_parser import parse_gcode, getStartToEnd

"""! @file
     @brief Python code to turn g-code into xy coordinates so the printer understands it.
"""


def toFile(data):
    with open("new_gcode.txt", 'w') as file:
        for i, line in enumerate(data):
            if i == 0:
                file.write(f"G0 X{line[0].X} Y{line[0].Y}\n")
            if not (line[0].X == data[i-1][0].X and line[0].Y == data[i-1][0].Y):
                file.write(f"G0 X{line[0].X} Y{line[0].Y}\n")
            file.write(f"G1 X{line[1].X} Y{line[1].Y}\n")

def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def optimize(lines):
    new_lines = []
    current_loc = [0, 0]

    l = len(lines)
    while l > 0:
        shortest_line = None
        shortest_dist = float('inf')
        for i in range(l):
            dist = calculateDistance(current_loc[0], current_loc[1], lines[i][0].X, lines[i][0].Y)
            if dist < shortest_dist:
                shortest_dist = dist
                shortest_line = i

        new_lines.append(lines[shortest_line])
        print(shortest_line, len(lines))
        current_loc = [lines[shortest_line][1].X, lines[shortest_line][1].Y]
        lines.pop(shortest_line)
        l -= 1
    
    return new_lines


coords = parse_gcode()
lijnen = getStartToEnd(coords)
optimized = optimize(lijnen)
toFile(optimized)
