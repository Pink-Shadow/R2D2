import os
from re import L, U
from sys import maxsize
import numpy as np
import matplotlib.pyplot as plt

listOfdict = []
max_steps = 0;
max_time = 0;

for file_name in os.listdir("./original"):
    if(file_name.endswith(".txt")) and not "output_ORIGINAL" in file_name:
        file = open("./original/" + file_name, "r")
        nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
        dictionary = {"file_name": file_name, "Gcode lines": len(nonempty_lines)}
        listOfdict.append(dictionary)
        file.close()

# load txt files with gcode
with open("./original/output_ORIGINAL_STEPS.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["original_STEPS"] = int(line[1])
                if int(line[1]) > max_steps:
                    max_steps = int(line[1])  


with open("./original/output_ORIGINAL_TIME.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["original_TIME"] = int(line[1])/1000000
                if int(line[1])/1000000 > max_time:
                    max_time = int(line[1])/1000000
        
current_file = ""
gemiddelde_duur = 0
tijden = []

with open("./NNA_logging2.txt", "r") as f:
    for line in f:
        if line.startswith("Bestand: "):
            line = line.split()
            current_file = line[1]
        elif line.startswith("Gemiddelde_duur: "):
            line = line.split()
            gemiddelde_duur = float(line[1])
        elif line.startswith("Tijdenlijst: "):
            line = line.split(": ")[1]
            line = line[1:-2]
            for tijd in line.split(", "):
                tijden.append(float(tijd))
            for i in listOfdict:
                if i["file_name"] == current_file:
                    i["GEM_CALCULATION_TIME"] = gemiddelde_duur
                    i["NNA_CALCULATION_TIME_list"] = tijden
            current_file = ""
            gemiddelde_duur = 0
            tijden = []

# load txt files with gcode
with open("./NNA/output_NNA_STEPS.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["NNA_STEPS"] = int(line[1])
                if int(line[1]) > max_steps:
                    max_steps = int(line[1])


# load txt files with gcode
with open("./NNA/output_NNA_TIME.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["NNA_DRAW_TIME"] = int(line[1])/1000000
                i["NNA_TOTAL_TIME"] = int(line[1])/1000000 + i["GEM_CALCULATION_TIME"]
                i["NNA_TOTAL_TIME_list"] = []
                for tijd in i["NNA_CALCULATION_TIME_list"]:
                     i["NNA_TOTAL_TIME_list"].append(int(line[1])/1000000 + tijd)
                if max(i["NNA_TOTAL_TIME_list"]) > max_time:
                    max_time = max(i["NNA_TOTAL_TIME_list"])
                

# load txt files with gcode

with open("./PYTHON_TSP/output_TSP_PYTHON_STEPS.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        line[0] = line[0].split("_", 1)[1]
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("TSP_STEPS"):
                    i["TSP_STEPS"] = i["TSP_STEPS"] + int(line[1])
                    i["TSP_STEPS_list"].append(int(line[1]))
                else:
                    i["TSP_STEPS"] = int(line[1])
                    i["TSP_STEPS_list"] = [int(line[1])]

# load txt files with gcode

with open("./PYTHON_TSP/output_TSP_PYTHON_TIME.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        line[0] = line[0].split("_", 1)[1]
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("TSP_DRAW_TIME"):
                    i["TSP_DRAW_TIME"] = i["TSP_DRAW_TIME"] + int(line[1])/1000000
                    i["TSP_TOTAL_TIME"] = i["TSP_TOTAL_TIME"] + int(line[1])/1000000 + i["GEM_CALCULATION_TIME"]
                    i["TSP_DRAW_TIME_list"].append(int(line[1])/1000000)
                else:
                    i["TSP_DRAW_TIME"] = int(line[1])/1000000
                    i["TSP_TOTAL_TIME"] = int(line[1])/1000000 + i["GEM_CALCULATION_TIME"]
                    i["TSP_DRAW_TIME_list"] = [int(line[1])/1000000]

# load txt files with gcode

with open("./NNA_PYTHON_TSP/output_NNA_TSP_PYTHON_STEPS.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        line[0] = line[0].split("_", 1)[1]
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("NNA_TSP_STEPS"):
                    i["NNA_TSP_STEPS"] = i["NNA_TSP_STEPS"] + int(line[1])
                    i["NNA_TSP_STEPS_list"].append(int(line[1]))
                else:
                    i["NNA_TSP_STEPS"] = int(line[1])
                    i["NNA_TSP_STEPS_list"] = [int(line[1])]
# load txt files with gcode

with open("./NNA_PYTHON_TSP/output_NNA_TSP_PYTHON_TIME.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        line[0] = line[0].split("_", 1)[1]
        for i in listOfdict:
            if i["file_name"] == line[0]:
                if i.keys().__contains__("NNA_TSP_TOTAL_TIME"):
                    i["NNA_TSP_TOTAL_TIME"] = i["NNA_TSP_TOTAL_TIME"] + int(line[1])/1000000 + i["GEM_CALCULATION_TIME"]*2
                    i["NNA_TSP_DRAW_TIME"] = i["NNA_TSP_DRAW_TIME"] + int(line[1])/1000000
                    i["NNA_TSP_DRAW_TIME_list"].append(int(line[1])/1000000)
                else:
                    i["NNA_TSP_TOTAL_TIME"] = int(line[1])/1000000 + i["GEM_CALCULATION_TIME"]*2
                    i["NNA_TSP_DRAW_TIME"] = int(line[1])/1000000 + i["GEM_CALCULATION_TIME"]
                    i["NNA_TSP_DRAW_TIME_list"] = [int(line[1])/1000000]       



for i in listOfdict:
    try:
        i["NNA_TIME_stddev"] = np.std(i["NNA_TOTAL_TIME_list"])
        i["TSP_STEPS"] = i["TSP_STEPS"] / 20
        i["TSP_DRAW_TIME"] = i["TSP_DRAW_TIME"] / 20
        i["TSP_TOTAL_TIME"] = i["TSP_TOTAL_TIME"] / 20
        i["NNA_TSP_STEPS"] = i["NNA_TSP_STEPS"] / 20
        i["NNA_TSP_TOTAL_TIME"] = i["NNA_TSP_TOTAL_TIME"] / 20
        i["NNA_TSP_DRAW_TIME"] = i["NNA_TSP_DRAW_TIME"] / 20
        
        
        if i["TSP_STEPS"] > max_steps:
            max_steps = i["TSP_STEPS"]
        if i["TSP_TOTAL_TIME"] > max_time:
            max_time = i["TSP_TOTAL_TIME"]
        if i["NNA_TSP_STEPS"] > max_steps:
            max_steps = i["NNA_TSP_STEPS"]
        if i["NNA_TSP_TOTAL_TIME"] > max_time:
            max_time = i["NNA_TSP_TOTAL_TIME"]
        
        i["TSP_STEPS_stddev"] = np.std(i["TSP_STEPS_list"])
        i["TSP_TIME_stddev"] = np.std(i["TSP_DRAW_TIME_list"])
        i["NNA_TSP_STEPS_stddev"] = np.std(i["NNA_TSP_STEPS_list"])
        i["NNA_TSP_TIME_stddev"] = np.std(i["NNA_TSP_DRAW_TIME_list"])
    except KeyboardInterrupt:
        print("error: ", i["file_name"])
with open("./PYTHON_TSP/objects.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        for i in listOfdict:
            if i["file_name"] == line[0]:
                i["Objects"] = int(line[2])

listOfdict = sorted(listOfdict, key=lambda d: d['Gcode lines'])

original_STEPS = []
NNA_STEPS = []
TSP_STEPS = []
TSP_STEPS_ERROR = []
NNA_TSP_STEPS = []
NNA_TSP_STEPS_ERROR = []


names = []
for i in listOfdict:
    original_STEPS.append(i["original_STEPS"])
    NNA_STEPS.append(i["NNA_STEPS"])
    TSP_STEPS.append(i["TSP_STEPS"])
    TSP_STEPS_ERROR.append(i["TSP_STEPS_stddev"])
    NNA_TSP_STEPS.append(i["NNA_TSP_STEPS"])
    NNA_TSP_STEPS_ERROR.append(i["NNA_TSP_STEPS_stddev"])
    names.append(str(i["Gcode lines"]) + "\n" + i["file_name"][:-4])

# PLOT
fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])
ax.grid(axis = 'y')

width = 0.2
ticks = np.arange(len(listOfdict))
ax.bar(ticks, original_STEPS, width, label='Original')
ax.bar(ticks + width, NNA_STEPS, width, align="center", label='NNA')
ax.bar(ticks + width * 2, TSP_STEPS, width, label='TSP', yerr=TSP_STEPS_ERROR, capsize=5)
ax.bar(ticks + width * 3, NNA_TSP_STEPS, width, label='NNA_TSP', yerr=NNA_TSP_STEPS_ERROR, capsize=5)


ax.set_ylabel('Number of steps')
ax.set_title('Steps per Algorithm')
steps = range(0, int(max_steps)+500000, 500000)
ax.set_yticks(steps)
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('Number of G-code lines')
ax.legend(loc='best')
plt.savefig('HistogramImprovement_lines.png')
plt.show()


listOfdict = sorted(listOfdict, key=lambda d: d['Objects'])

original_STEPS = []
NNA_STEPS = []
TSP_STEPS = []
TSP_STEPS_ERROR = []
NNA_TSP_STEPS = []
NNA_TSP_STEPS_ERROR = []


names = []
for i in listOfdict:
    original_STEPS.append(i["original_STEPS"])
    
    NNA_STEPS.append(i["NNA_STEPS"])
    TSP_STEPS.append(i["TSP_STEPS"])
    TSP_STEPS_ERROR.append(i["TSP_STEPS_stddev"])
    NNA_TSP_STEPS.append(i["NNA_TSP_STEPS"])
    NNA_TSP_STEPS_ERROR.append(i["NNA_TSP_STEPS_stddev"])

    names.append(str(i['Objects']) + "\n" + i["file_name"][:-4])


# PLOT
fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])
ax.grid(axis = 'y')


width = 0.2
ticks = np.arange(len(listOfdict))
ax.bar(ticks, original_STEPS, width, label='Original')
ax.bar(ticks + width, NNA_STEPS, width, align="center", label='NNA')
ax.bar(ticks + width * 2, TSP_STEPS, width, label='TSP', yerr=TSP_STEPS_ERROR, capsize=5)
ax.bar(ticks + width * 3, NNA_TSP_STEPS, width, label='NNA_TSP', yerr=NNA_TSP_STEPS_ERROR, capsize=5)

ax.set_ylabel('Number of steps')
ax.set_title('Steps per Algorithm')
ax.set_yticks(range(0, int(max_steps)+500000, 500000))
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('Number of objects')
ax.legend(loc='best')
plt.savefig('HistogramImprovement_objects.png')
plt.show()

listOfdict = sorted(listOfdict, key=lambda d: d['original_TIME'])

original_TIME = []
NNA_CALCULATION_TIME = []
NNA_CALCULATION_TIME_ERROR = []
NNA_DRAW_TIME = []
TSP_DRAW_TIME = []
TSP_CALCULATION_TIME = []
TSP_DRAW_ERROR = []

NNA_TSP_DRAW_TIME = []

NNA_TSP_NNA_CALCULATION_TIME = []
NNA_TSP_NNA_CALCULATION_TIME_ERROR = []

NNA_TSP_TSP_CALCULATION_TIME = []
NNA_TSP_DRAW_ERROR = []



names = []

for i in listOfdict:
    original_TIME.append(i["original_TIME"])
    NNA_CALCULATION_TIME.append(i["GEM_CALCULATION_TIME"] + i["NNA_DRAW_TIME"])
    NNA_CALCULATION_TIME_ERROR.append(np.std(i["NNA_CALCULATION_TIME_list"]))
    NNA_DRAW_TIME.append(i["NNA_DRAW_TIME"])

    names.append(str(i["Gcode lines"]) + "\n" + i["file_name"][:-4])
    
    TSP_CALCULATION_TIME.append(i["GEM_CALCULATION_TIME"])
    TSP_DRAW_TIME.append(i["TSP_DRAW_TIME"] + i["GEM_CALCULATION_TIME"])
    TSP_DRAW_ERROR.append(i["TSP_TIME_stddev"])
    
    NNA_TSP_NNA_CALCULATION_TIME.append(i["GEM_CALCULATION_TIME"]*2)
    NNA_TSP_NNA_CALCULATION_TIME_ERROR.append(np.std(i["NNA_CALCULATION_TIME_list"]))
    NNA_TSP_TSP_CALCULATION_TIME.append(i["GEM_CALCULATION_TIME"])
    NNA_TSP_DRAW_TIME.append(i["NNA_TSP_DRAW_TIME"] + i["GEM_CALCULATION_TIME"]*2)
    
    NNA_TSP_DRAW_ERROR.append(i["NNA_TSP_TIME_stddev"])

# PLOT
fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])
ax.grid(axis = 'y')

width = 0.2
ticks = np.arange(len(listOfdict))
ax.bar(ticks, original_TIME, width, label='Original drawing time')
ax.bar(ticks + width, NNA_CALCULATION_TIME, width, label='NNA calculation time', yerr=NNA_CALCULATION_TIME_ERROR, capsize=5)
ax.bar(ticks + width, NNA_DRAW_TIME, width, label='NNA drawing time')

ax.bar(ticks + width * 2, TSP_DRAW_TIME, width, label='TSP drawing time', yerr=TSP_DRAW_ERROR, capsize=5)
ax.bar(ticks + width * 2, TSP_CALCULATION_TIME, width, label='TSP calculation time')

ax.bar(ticks + width * 3, NNA_TSP_DRAW_TIME, width, label='NNA_TSP drawing time', yerr=NNA_TSP_DRAW_ERROR, capsize=5)
ax.bar(ticks + width * 3, NNA_TSP_NNA_CALCULATION_TIME, width, label='NNA_TSP NNA calculation time', yerr=NNA_CALCULATION_TIME_ERROR, capsize=5)
ax.bar(ticks + width * 3, NNA_TSP_TSP_CALCULATION_TIME, width, label='NNA_TSP TSP calculation time')

ax.set_ylabel('time in S')
ax.set_title('Time per Algorithm (Calculation time + drawing time)')
ax.set_yticks(range(0, int(max_time)+200, 100))
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('Number of lines')
ax.legend(loc='best')
plt.savefig('HistogramImprovement_time.png')
plt.show()