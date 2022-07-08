import math
from gcode_parser import parse_gcode, getStartToEnd
import os
import time
import copy

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
    with open("Test_q31123.txt", 'w') as logging:
        new_lines = []
        current_loc = [30000, 25000]

        l = len(lines)

        count_breaks = 0
        checks_skipped = 0
        logging.write(f"starts with {l} lines")
        prev_line = 0
        loops_past_0=0
        while l > 0:
            shortest_line = None
            shortest_dist = float('inf')
            for i in range(l):
                index = (i+prev_line)%l
                if (index==0):
                    loops_past_0+=1
                dist = calculateDistance(current_loc[0], current_loc[1], lines[index][0].X, lines[index][0].Y)
                if dist < shortest_dist:
                    shortest_dist = dist
                    shortest_line = index
                if dist == 0:
                    count_breaks += 1
                    checks_skipped += l - i
                    break
            new_lines.append(lines[shortest_line])
            if len(lines) % 500 == 0:
                logging.write(f"{len(lines)} lines left")
                logging.write(f"{count_breaks} breaks")
                logging.write(f"{checks_skipped} checks skipped")
                logging.write(f"{loops_past_0} loops came across index 0\n\n\n\n")
            current_loc = [lines[shortest_line][1].X, lines[shortest_line][1].Y]
            lines.pop(shortest_line)
            prev_line=shortest_line
            l -= 1
        logging.write(f"{len(lines)} lines left")
        logging.write(f"{count_breaks} breaks")
        logging.write(f"{checks_skipped} checks skipped")
        logging.write(f"{loops_past_0} loops came across index 0")
        return new_lines

if __name__ == "__main__":
    for file_name in os.listdir("./original"):
        if file_name.endswith(".txt") and file_name == "leeuw.txt":
            print(file_name)
            coords = parse_gcode("./original/" + file_name)
            lijnen = getStartToEnd(coords)
            tijden_lijst = []
            for i in range(1):
                print("Iterations left: {}".format(i))
                lijnen_copy = copy.deepcopy(lijnen)
                beginTijd = time.time()
                optimized = optimize(lijnen_copy)
                eindTijd = time.time()
                tijden_lijst.append(eindTijd - beginTijd)

            with open("NNA_logging2.txt", 'a') as file:
                file.write("Bestand: {}\nGemiddelde_duur: {} seconden\nTijdenlijst: {}\nMaximale verschil: {}\n\n\n\n\n\n".format(file_name, sum(tijden_lijst) / len(tijden_lijst), tijden_lijst, max(tijden_lijst)-min(tijden_lijst)))
            toFile(optimized, "./NNA/"+file_name)
