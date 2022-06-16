import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt

listOfdict = []

for file_name in os.listdir("./original"):
    file = open("./original/" + file_name, "r")
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    dictionary = {"file_name": file_name, "Gcode lines": len(nonempty_lines)}
    listOfdict.append(dictionary)
    file.close()

# load txt files with gcode
for file_name in os.listdir("./original"):
    tmp = subprocess.run(['CalculateSteps.exe', "./original/" + file_name], stdout=subprocess.PIPE)
    for i in listOfdict:
        if i["file_name"] == file_name:
            i["original"] = int(tmp.stdout)

print("Original done")

# load txt files with gcode
for file_name in os.listdir("./NNA"):
    tmp = subprocess.run(['CalculateSteps.exe', "./NNA/" + file_name], stdout=subprocess.PIPE)
    for i in listOfdict:
        if i["file_name"] == file_name:
            i["NNA"] = int(tmp.stdout)

print("NNA done")

# load txt files with gcode
for file_name in os.listdir("./TSP"):
    tmp2 = 0
    for iteration in range(0, 1):
        tmp = subprocess.run(['CalculateSteps.exe', "./TSP/" + file_name], stdout=subprocess.PIPE)
        tmp2 += int(tmp.stdout)
    tmp2 = tmp2 / 1
    for i in listOfdict:
        if i["file_name"] == file_name:
            i["TSP"] = int(tmp2)

print("TSP done")

# load txt files with gcode and get gcode line count
for file_name in os.listdir("./custom"):
    tmp2 = 0
    for iteration in range(0, 1):
        tmp = subprocess.run(['CalculateSteps.exe', "./custom/" + file_name], stdout=subprocess.PIPE)
        tmp2 += int(tmp.stdout)
    tmp2 = tmp2 / 1
    for i in listOfdict:
        if i["file_name"] == file_name:
            i["custom"] = int(tmp2)

print(listOfdict)
listOfdict = sorted(listOfdict, key=lambda d: d['Gcode lines'])
print(listOfdict)

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
plt.show()
