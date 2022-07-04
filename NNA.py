import math
from gcode_parser import parse_gcode, getStartToEnd
import os

"""! @file
     @brief Python code to turn g-code into xy coordinates so the printer understands it.
"""


def toFile(data, file_name):
    with open(file_name, 'w') as file:
        for i, line in enumerate(data):
            # check if start en end are the same
            if line[0].X == line[1].X and line[0].Y == line[1].Y:
                continue
            if i == 0:
                file.write(f"G0 X{line[0].X} Y{line[0].Y}\n")
            elif not (line[0].X == data[i - 1][1].X and line[0].Y == data[i - 1][1].Y):
                file.write(f"G0 X{line[0].X} Y{line[0].Y}\n")
            file.write(f"G1 X{line[1].X} Y{line[1].Y}\n")


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def optimize(lines):
    new_lines = []
    current_loc = [30000, 25000]

    l = len(lines)

    count_breaks = 0
    checks_skipped = 0
    print(f"starts with {l} lines")
    while l > 0:
        shortest_line = None
        shortest_dist = float('inf')
        for i in range(l):
            dist = calculateDistance(current_loc[0], current_loc[1], lines[i][0].X, lines[i][0].Y)
            if dist < shortest_dist:
                shortest_dist = dist
                shortest_line = i
            if dist == 0:
                count_breaks += 1
                checks_skipped += l - i
                break
        new_lines.append(lines[shortest_line])
        if len(lines) % 500 == 0:
            print(f"{len(lines)} lines left")
        current_loc = [lines[shortest_line][1].X, lines[shortest_line][1].Y]
        lines.pop(shortest_line)
        l -= 1
    print(f"{len(lines)} lines left")
    print(f"{count_breaks} breaks")
    print(f"{checks_skipped} checks skipped")
    return new_lines

if __name__ == "__main__":
    for file_name in os.listdir("./original"):
        print(file_name)
        coords = parse_gcode("./original/" + file_name)
        lijnen = getStartToEnd(coords)
        optimized = optimize(lijnen)
        toFile(optimized, "./NNA/"+file_name)
