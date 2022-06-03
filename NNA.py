import math

"""! @file
     @brief Python code to turn g-code into xy coordinates so the printer understands it.
"""

optimizedLines = []

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def optimize(lines):
    current_x = 0
    current_y = 0
    lineNumber = 0
    tmpDistance = 30000
    tmpShortest = []
    distance = 0
    for i in range(len(lines)):

        x = int(lines[i][0][1][0])
        y = int(lines[i][0][1][1])

        distance = calculateDistance(current_x, current_y, x, y)

        if(distance < tmpDistance):
            tmpDistance = distance
            tmpShortest = lines[i]
            lineNumber = i

    print(tmpDistance)
    print(('0', [current_x, current_y]), tmpShortest[0])

    if(distance == 0):
        optimizedLines.append(tmpShortest)
        lines.pop(lineNumber)
    else:
        optimizedLines.append( (('0', [current_x, current_y]), tmpShortest[0]) )
        optimizedLines.append(tmpShortest)
        lines.pop(lineNumber)

    print(optimizedLines)



def getStartToEnd(coords):
    current = 0
    next = 0
    tmp = []
    listWithLines = []
    for x in range(len(coords)-1):
        if(coords[x+1][0] != '0'):
            tmp.append(coords[x])
            tmp.append(coords[x+1])
            listWithLines.append(tmp)
            tmp = []

    return listWithLines


def readGcode(filename):
    """!
    @brief Read the g-code and set it to xy coords.
    @param coords this is where the coords are saved in.
    @details Reads the file with g-codes and checks for every line what the G number is and what the X and Y are. Then appends this split to an array.
    @return returns new array with shape: g-code number, X, Y.
    """

    coords = []
    with open(f"{filename}", "r") as gcode:
        data = gcode.readlines()
        for i in data:
            tmp = []
            tmp_g = ''
            elements = i.split(' ')
            for e in elements:
                c = e[0]

                if c == 'X':
                    tmp.append(e.strip()[1:])
                if c == 'Y':
                    tmp.append(e.strip()[1:])
                if c == 'G' and len(elements) > 1:
                    tmp_g = e.strip()[1:]

            if len(tmp) > 0 and len(tmp_g) > 0:
                coords.append((tmp_g, tmp))
            elif len(tmp) == 0 and len(tmp_g) > 0:
                coords.append((tmp_g))

    return coords


coords = readGcode("gcode.txt")
lines = getStartToEnd(coords)
optimize(lines)
