import os
from sys import maxsize
import numpy as np
import matplotlib.pyplot as plt

listOfdict = []
max_steps = 0;

for file_name in os.listdir("./original"):
    if(file_name.endswith(".txt")) and not "output_ORIGINAL" in file_name:
        file = open("./original/" + file_name, "r")
        nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
        dictionary = {"file_name": file_name, "Gcode lines": len(nonempty_lines)}
        listOfdict.append(dictionary)
        file.close()

# load txt files with gcode
with open("./original/output_ORIGINAL.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["original"] = int(line[1])
                if int(line[1]) > max_steps:
                    max_steps = int(line[1])


# load txt files with gcode
with open("./NNA/output_NNA.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["NNA"] = int(line[1])
                if int(line[1]) > max_steps:
                    max_steps = int(line[1])

# load txt files with gcode

with open("./PYTHON_TSP/output_TSP_PYTHON.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        line[0] = line[0].split("_", 1)[1]
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("TSP"):
                    i["TSP"] = i["TSP"] + int(line[1])
                    i["TSP_list"].append(int(line[1]))
                else:
                    i["TSP"] = int(line[1])
                    i["TSP_list"] = [int(line[1])]

for i in listOfdict:
    try:
        i["TSP"] = i["TSP"] / 20
        if i["TSP"] > max_steps:
            max_steps = i["TSP"]
        i["TSP_stddev"] = np.std(i["TSP_list"])
    except KeyError:
        print(i["file_name"])
with open("./PYTHON_TSP/objects.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["Objects"] = int(line[2])

listOfdict = sorted(listOfdict, key=lambda d: d['Gcode lines'])

original = []
NNA = []
TSP = []
TSP_ERROR = []
names = []
for i in listOfdict:
    original.append(i["original"])
    NNA.append(i["NNA"])
    TSP.append(i["TSP"])
    TSP_ERROR.append(i["TSP_stddev"])
    names.append(str(i["Gcode lines"]) + "\n" + i["file_name"][:-4])


# PLOT
fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])

width = 0.2
ticks = np.arange(len(listOfdict))
ax.bar(ticks, original, width, label='Original')
ax.bar(ticks + width, NNA, width, align="center", label='NNA')
ax.bar(ticks + width * 2, TSP, width, label='TSP', yerr=TSP_ERROR, capsize=5)

ax.set_ylabel('Number of steps')
ax.set_title('Steps per Algorithm')
ax.set_yticks(range(0, int(max_steps)+500000, 500000))
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('Number of G-code lines')
ax.legend(loc='best')
plt.savefig('HistogramImprovement_lines.png')
plt.show()


listOfdict = sorted(listOfdict, key=lambda d: d['Objects'])

original = []
NNA = []
TSP = []
TSP_ERROR = []
names = []
for i in listOfdict:
    original.append(i["original"])
    NNA.append(i["NNA"])
    TSP.append(i["TSP"])
    TSP_ERROR.append(i["TSP_stddev"])
    names.append(str(i["Objects"]) + "\n" + i["file_name"][:-4])


# PLOT
fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])

width = 0.2
ticks = np.arange(len(listOfdict))
ax.bar(ticks, original, width, label='Original')
ax.bar(ticks + width, NNA, width, align="center", label='NNA')
ax.bar(ticks + width * 2, TSP, width, label='TSP', yerr=TSP_ERROR, capsize=5)

ax.set_ylabel('Number of steps')
ax.set_title('Steps per Algorithm')
ax.set_yticks(range(0, int(max_steps)+500000, 500000))
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('Number of objects')
ax.legend(loc='best')
plt.savefig('HistogramImprovement_objects.png')
plt.show()