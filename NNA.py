import copy
import math
import parser

"""! @file
     @brief Python code to turn g-code into xy coordinates so the printer understands it.
"""


def toFile(data):
    file = open("new_gcode.txt", 'w')
    for line in data:
        file.write(str(line))
        file.write("\n")
    file.close()


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def optimize(lines):
    linesToPop = copy.deepcopy(lines)

    newGcode = []
    index = 0
    tmpclass = parser.gcode_class()
    shortestLine = parser.gcode_class()
    len_lines = len(lines) -1

    while len_lines:
        added = False
        distanceNotNull = False
        lastDistance = 30000
        print(len_lines)
        currentXbegin = lines[len_lines][0].X
        currentXend = lines[len_lines][1].X
        currentYbegin = lines[len_lines][0].Y
        currentYend = lines[len_lines][1].Y

        for i in range(len(linesToPop)):
            added = False
            if (currentXend == lines[i][1].X & currentYend == lines[i][1].Y) & (
                    currentXbegin == lines[i][0].X & currentYbegin == lines[i][0].Y):
                # gelijk aan zichzelf (eindpunten
                # print("if ")
                # shortestIndex = i

                continue

            elif (currentXend == lines[i][0].X):
                if (currentYend == lines[i][0].Y):
                    # aan elkaar vast
                    tmpclass.G = 1
                    tmpclass.X = currentXend
                    tmpclass.Y = currentYend
                    newGcode.append(copy.copy(tmpclass))
                    print("g1 eindpunt current", tmpclass)
                    print(f"g1 beginpunt nieuw G1 X{lines[i][0].X} Y{lines[i][0].Y}")

                    tmpclass.G = 1
                    tmpclass.X = lines[i][1].X
                    tmpclass.Y = lines[i][1].Y
                    newGcode.append(copy.copy(tmpclass))
                    print("g1 eindpunt new", tmpclass)

                    index = i

                    added = True
                    break

            else:

                distance = calculateDistance(currentXend, currentYend, lines[i][0].X, lines[i][0].Y)
                # print(f"distance {distance}, last {lastDistance}")
                if distance < lastDistance:
                    lastDistance = distance
                    shortestLine = lines[i][0]
                    index = i
                    added = False
        # print(distanceNotNull)
        if not added:
            # print(distanceNotNull)
            # print("else")
            tmpclass.G = 0
            tmpclass.X = shortestLine.X
            tmpclass.Y = shortestLine.Y
            newGcode.append(copy.copy(tmpclass))
            newGcode.append(copy.copy(shortestLine))
            print("g0 korte", shortestLine)
        linesToPop[index] = 0

        len_lines -= 1
    return newGcode


coords = parser.parse_gcode()

lijnen = parser.getStartToEnd(coords)
# for x in lijnen:
#     print(x)

optimized = optimize(lijnen)
#
# for x in optimized:
#     print(x)
# print(lines)
toFile(optimized)
