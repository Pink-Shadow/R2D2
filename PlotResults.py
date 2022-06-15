import subprocess
import os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

numberOfImages = 14

original = []
# load txt files with gcode
for file_name in os.listdir("./original"):
    tmp = subprocess.run(['CalculateSteps.exe', "./original/"+file_name], stdout=subprocess.PIPE)
    original.append(int(tmp.stdout))

print("Original done")

NNA = []
# load txt files with gcode
for file_name in os.listdir("./NNA"):
    tmp = subprocess.run(['CalculateSteps.exe', "./NNA/"+file_name], stdout=subprocess.PIPE)
    NNA.append(int(tmp.stdout))

print("NNA done")
    
TSP = []
# load txt files with gcode
for file_name in os.listdir("./TSP"):
    tmp2 = 0
    for iteration in range(0,1):
        tmp = subprocess.run(['CalculateSteps.exe', "./TSP/"+file_name], stdout=subprocess.PIPE)
        tmp2 += int(tmp.stdout)
    tmp2 = tmp2/1
    TSP.append(tmp2)

print("TSP done")


custom = []
# load txt files with gcode
for file_name in os.listdir("./custom"):
    tmp2 = 0
    for iteration in range(0,1):
        tmp = subprocess.run(['CalculateSteps.exe', "./custom/"+file_name], stdout=subprocess.PIPE)
        tmp2 += int(tmp.stdout)
    tmp2 = tmp2/1
    custom.append(tmp2)

print("Custom done")




# #PLOT

names = ('aston', 'cat', 'dog', 'elephant',
         'f1', 'ferarri', 'lambo', 'leeuw', 'mondr_1', 'mondr_2', 'mondr_3', 'mondr_4', 'mondr_5', 'pug')


fig = plt.figure(figsize=(20, 10))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])

width = 0.2
ticks = np.arange(len(names))
ax.bar(ticks, original, width, label='Original')
ax.bar(ticks + width, NNA, width, align="center",label='NNA')
ax.bar(ticks + width * 2, TSP, width, label='TSP')
ax.bar(ticks + width * 3, custom, width, align="center",label='Custom')

ax.set_ylabel('Steps * 10^7')
ax.set_title('Steps per Algorithm')
ax.set_yticks(range(0, max(original)+1000000, 500000))
ax.set_xticks(ticks + 0.30)
ax.set_xticklabels(names)
ax.set_xlabel('File Name')

ax.legend(loc='best')
plt.show()