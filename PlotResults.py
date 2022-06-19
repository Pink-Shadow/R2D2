import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt

listOfdict = []

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


# load txt files with gcode
with open("./NNA/output_NNA.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["NNA"] = int(line[1])

# load txt files with gcode

with open("./TSP_res/output_TSPRES.txt", "r") as f:
    for line in f:
        line = line.split()
        line[0] = line[0].split("\\")[0] + ".txt"
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("TSP"):
                    i["TSP"] = i["TSP"] + int(line[1])
                else:
                    i["TSP"] = int(line[1])

for i in listOfdict:
    i["TSP"] = i["TSP"] / 20

with open("./TSP_MUT/output_TSPMUT.txt", "r") as f:
    for line in f:
        line = line.split()
        line[0] = line[0].split("\\")[0] + ".txt"
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("custom"):
                    i["custom"] = i["custom"] + int(line[1])
                else:
                    i["custom"] = int(line[1])
for i in listOfdict:
    i["custom"] = i["custom"] / 20

listOfdict = sorted(listOfdict, key=lambda d: d['Gcode lines'])

original = []
for i in listOfdict:
    original.append(i["original"])

NNA = []
for i in listOfdict:
    NNA.append(i["NNA"])
TSP = []
for i in listOfdict:
    TSP.append(i["TSP"])
custom = []
for i in listOfdict:
    custom.append(i["custom"])
names = []
for i in listOfdict:
    names.append(i["Gcode lines"])


# PLOT
fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])

width = 0.2
ticks = np.arange(len(listOfdict))
ax.bar(ticks, original, width, label='Original')
ax.bar(ticks + width, NNA, width, align="center", label='NNA')
ax.bar(ticks + width * 2, TSP, width, label='TSP')
ax.bar(ticks + width * 3, custom, width, align="center", label='Custom')

ax.set_ylabel('Number of steps')
ax.set_title('Steps per Algorithm')
ax.set_yticks(range(0, 13000000 + 1000000, 500000))
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('Number of G-code lines')
ax.legend(loc='best')
plt.savefig('HistogramImprovement.png')
plt.show()
