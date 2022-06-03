import copy
import math
import parser

"""! @file
     @brief Python code to turn g-code into xy coordinates so the printer understands it.
"""


def toFile(lines):
    file = open("new_gcode.txt", 'w')
    for line in lines:
        file.write(str(line))
        file.write("\n")
    file.close()


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return dist


def optimize(lines):

    newGcode = []
    index = 0
    tmpclass = parser.gcode_class()

    while len(lines) != 0:
        distanceNotNull = False
        distance = 0
        shortestIndex = 0
        lastDistance = 30000
        currentX = lines[shortestIndex][1].X
        currentY = lines[shortestIndex][1].Y
        lines.pop(shortestIndex)
        for i in range(len(lines)):
            if currentX == lines[i][1].X and currentY == lines[i][1].Y:
                # print("if ")
                # shortestIndex = i
                continue

            elif currentX == lines[i][0].X and currentY == lines[i][0].Y:
                # print("elif")
                # tmpclass.G = 1
                # tmpclass.X = currentX
                # tmpclass.Y = currentY
                # newGcode.append(copy.copy(tmpclass))
                tmpclass.G = 1
                tmpclass.X = lines[i][1].X
                tmpclass.Y = lines[i][1].Y
                newGcode.append(copy.copy(tmpclass))
                shortestIndex = i
            else:

                distance = calculateDistance(currentX, currentY, lines[i][0].X, lines[i][0].Y)

                if distance < lastDistance:
                    distanceNotNull = True
                    # print("else")
                    lastDistance = distance
                    shortestIndex = i

        if distanceNotNull:
            distanceNotNull = False
            tmpclass.G = 0
            tmpclass.X = lines[shortestIndex][1].X
            tmpclass.Y = lines[shortestIndex][1].Y
            newGcode.append(copy.copy(tmpclass))

    return newGcode


        

    # optimizedLines = []
    # current_x = 0
    # current_y = 0
    # while len(lines) != 0:
    #     lineNumber = 0
    #     tmpDistance = 30000
    #     tmpShortest = parser.gcode_class()
    #     distance = 0
    #     for i in range(len(lines)):
    #
    #         x = lines[i][0].X
    #         y = lines[i][0].Y
    #
    #         if (current_x == x) and (current_y == y):
    #             # # vast aan elkaar
    #             # lineNumber = i
    #             # optimizedLines.append(lines[lineNumber])
    #             # lines.pop(lineNumber)
    #             # current_x = x
    #             # current_y = y
    #             print("distance is 0")
    #             break
    #         else:
    #             # distance = calculateDistance(current_x, current_y, x, y)
    #             # if distance < tmpDistance:
    #             #     tmpDistance = distance
    #             #     tmpShortest = lines[i]
    #             #     lineNumber = i
    #             #
    #             #     tmpClass = parser.gcode_class()
    #             #     tmpClass.G = 0
    #             #     tmpClass.X = current_x
    #             #     tmpClass.Y = current_y
    #             #
    #             #     optimizedLines.append([tmpShortest[1], tmpClass])
    #             #     optimizedLines.append([tmpClass, tmpShortest[1]])
    #             #     lines.pop(lineNumber)
    #             #     print(distance)
    #             #     print("kort")
    #
    #         current_x = tmpShortest[i].X
    #         current_y = tmpShortest[i].Y
    #
    # # print(optimizedLines)
    # return optimizedLines


coords = parser.parse_gcode()
lines = parser.getStartToEnd(coords)
optimizedLines = optimize(lines)

# for x in optimizedLines:
    # print(x)
toFile(optimizedLines)
