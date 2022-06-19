from re import L
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import subprocess
import os

aston_lengths = []
cat_lengths = []
dog_lengths = []
elephant_lengths = []
f1_lengths = []
ferrari_lengths = []
lambo_lengths = []
leeuw_lengths = []
mondriaan_1_lengths = []
mondriaan_2_lengths = []
mondriaan_3_lengths = []
mondriaan_4_lengths = []
mondriaan_5_lengths = []
pug_lengths = []

for dir_name in os.listdir("./TSP_MUT"):
    if dir_name == "aston":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                aston_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "cat":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                cat_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "dog":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                dog_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "elephant":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                elephant_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "f1":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                f1_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "ferrari":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                ferrari_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "lambo":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                lambo_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "leeuw":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                leeuw_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "mondriaan_1":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                mondriaan_1_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "mondriaan_2":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                mondriaan_2_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "mondriaan_3":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                mondriaan_3_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "mondriaan_4":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                mondriaan_4_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "mondriaan_5":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                mondriaan_5_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
    elif dir_name == "pug":
        for file in os.listdir(f"./TSP_MUT/{dir_name}"):
            if file.endswith(".txt"):
                pug_lengths.append(int(subprocess.run(['CalculateSteps.exe', f"./TSP_MUT/{dir_name}/"  + file], stdout=subprocess.PIPE).stdout))
                    
# ### SHOW ALL GRAPHS ###
# domain = np.linspace(0, 13000000, 10000)
# std_val = [round(np.std(aston_lengths), 2), round(np.std(cat_lengths), 2), round(np.std(dog_lengths), 2), round(np.std(elephant_lengths), 2), round(np.std(f1_lengths), 2), round(np.std(ferrari_lengths), 2), round(np.std(lambo_lengths), 2), round(np.std(leeuw_lengths), 2), round(np.std(mondriaan_1_lengths), 2), round(np.std(mondriaan_2_lengths), 2), round(np.std(mondriaan_3_lengths), 2), round(np.std(mondriaan_4_lengths), 2), round(np.std(mondriaan_5_lengths), 2), round(np.std(pug_lengths), 2)]
# mean_val = [round(np.mean(aston_lengths), 2), round(np.mean(cat_lengths), 2), round(np.mean(dog_lengths), 2), round(np.mean(elephant_lengths), 2), round(np.mean(f1_lengths), 2), round(np.mean(ferrari_lengths), 2), round(np.mean(lambo_lengths), 2), round(np.mean(leeuw_lengths), 2), round(np.mean(mondriaan_1_lengths), 2), round(np.mean(mondriaan_2_lengths), 2), round(np.mean(mondriaan_3_lengths), 2), round(np.mean(mondriaan_4_lengths), 2), round(np.mean(mondriaan_5_lengths), 2), round(np.mean(pug_lengths), 2)]

# for mu, std in zip(mean_val, std_val):
#     if std == 0:
#         std = 100000
#     # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
#     probabilities = norm.pdf(domain, mu, std)
#     plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

# plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
# plt.xlabel("path length")
# plt.ylabel("Probability")
# plt.show()

########################

### SHOW ASTON GRAPH ###

min = np.min(aston_lengths)
max = np.max(aston_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(aston_lengths), 2)]
mean_val = [round(np.mean(aston_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.2, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("ASTON")
plt.savefig('./TSP_MUT_PLOTS/aston_standard_div.png')
plt.show()

########################

### SHOW CAT GRAPH ###

min = np.min(cat_lengths)
max = np.max(cat_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(cat_lengths), 2)]
mean_val = [round(np.mean(cat_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("CAT")
plt.savefig('./TSP_MUT_PLOTS/cat_standard_div.png')
plt.show()


########################

### SHOW DOG GRAPH ###

min = np.min(dog_lengths)
max = np.max(dog_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(dog_lengths), 2)]
mean_val = [round(np.mean(dog_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("DOG")
plt.savefig('./TSP_MUT_PLOTS/dog_standard_div.png')
plt.show()

########################

### SHOW ELEPHANT GRAPH ###

min = np.min(elephant_lengths)
max = np.max(elephant_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(elephant_lengths), 2)]
mean_val = [round(np.mean(elephant_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("ELEPHANT")
plt.savefig('./TSP_MUT_PLOTS/elephant_standard_div.png')
plt.show()

########################

### SHOW F1 GRAPH ###

min = np.min(f1_lengths)
max = np.max(f1_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(f1_lengths), 2)]
mean_val = [round(np.mean(f1_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("F1")
plt.savefig('./TSP_MUT_PLOTS/f1_standard_div.png')
plt.show()

########################

### SHOW ferrari GRAPH ###

min = np.min(ferrari_lengths)
max = np.max(ferrari_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(ferrari_lengths), 2)]
mean_val = [round(np.mean(ferrari_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("FERRARI")
plt.savefig('./TSP_MUT_PLOTS/ferrari_standard_div.png')
plt.show()

########################

### SHOW lambo GRAPH ###

min = np.min(lambo_lengths)
max = np.max(lambo_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(lambo_lengths), 2)]
mean_val = [round(np.mean(lambo_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("LAMBO")
plt.savefig('./TSP_MUT_PLOTS/lambo_standard_div.png')
plt.show()

########################

### SHOW leeuw GRAPH ###

min = np.min(leeuw_lengths)
max = np.max(leeuw_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(leeuw_lengths), 2)]
mean_val = [round(np.mean(leeuw_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("LEEUW")
plt.savefig('./TSP_MUT_PLOTS/leeuw_standard_div.png')
plt.show()

########################

### SHOW mondriaan_1 GRAPH ###

min = np.min(mondriaan_1_lengths)
max = np.max(mondriaan_1_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(mondriaan_1_lengths), 2)]
mean_val = [round(np.mean(mondriaan_1_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("MONDRIAAN_1")
plt.savefig('./TSP_MUT_PLOTS/mondriaan_1_standard_div.png')
plt.show()

########################

### SHOW mondriaan_2 GRAPH ###

min = np.min(mondriaan_2_lengths)
max = np.max(mondriaan_2_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(mondriaan_2_lengths), 2)]
mean_val = [round(np.mean(mondriaan_2_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("MONDRIAAN_2")
plt.savefig('./TSP_MUT_PLOTS/mondriaan_2_standard_div.png')
plt.show()

########################

### SHOW mondriaan_3 GRAPH ###

min = np.min(mondriaan_3_lengths)
max = np.max(mondriaan_3_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(mondriaan_3_lengths), 2)]
mean_val = [round(np.mean(mondriaan_3_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("MONDRIAAN_3")
plt.savefig('./TSP_MUT_PLOTS/mondriaan_3_standard_div.png')
plt.show()

########################

### SHOW mondriaan_4 GRAPH ###

min = np.min(mondriaan_4_lengths)
max = np.max(mondriaan_4_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(mondriaan_4_lengths), 2)]
mean_val = [round(np.mean(mondriaan_4_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("MONDRIAAN_4")
plt.savefig('./TSP_MUT_PLOTS/mondriaan_4_standard_div.png')
plt.show()

########################

### SHOW mondriaan_5 GRAPH ###

min = np.min(mondriaan_5_lengths)
max = np.max(mondriaan_5_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(mondriaan_5_lengths), 2)]
mean_val = [round(np.mean(mondriaan_5_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("MONDRIAAN_5")
plt.savefig('./TSP_MUT_PLOTS/mondriaan_5_standard_div.png')
plt.show()

########################

### SHOW pug GRAPH ###

min = np.min(pug_lengths)
max = np.max(pug_lengths)
r = max - min if max - min != 0 else max

domain = np.linspace(min-r/2, max+r/2, r//2)
std_val = [round(np.std(pug_lengths), 2)]
mean_val = [round(np.mean(pug_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.125, 1), ncol=2)
plt.xlabel("path length")
plt.ylabel("Probability")
plt.title("PUG")
plt.savefig('./TSP_MUT_PLOTS/pug_standard_div.png')
plt.show()