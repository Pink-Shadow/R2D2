import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np



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


with open('TSP_MUT/meta_data_tspmut.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line.strip()
        tmp = line.split(' ')
        if tmp[0] == 'aston.txt':
            aston_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'cat.txt':
            cat_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'dog.txt':
            dog_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'elephant.txt':
            elephant_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'f1.txt':
            f1_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'ferrari.txt':
            ferrari_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'lambo.txt':
            lambo_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'leeuw.txt':
            leeuw_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'mondriaan_1.txt':
            mondriaan_1_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'mondriaan_2.txt':
            mondriaan_2_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'mondriaan_3.txt':
            mondriaan_3_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'mondriaan_4.txt':
            mondriaan_4_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'mondriaan_5.txt':
            mondriaan_5_lengths.append(float(tmp[-3]))
        elif tmp[0] == 'pug.txt':
            pug_lengths.append(float(tmp[-3]))
        
        
domain = np.linspace(0, 8000000, 10000)
std_val = [round(np.std(aston_lengths), 2), round(np.std(cat_lengths), 2), round(np.std(dog_lengths), 2), round(np.std(elephant_lengths), 2), round(np.std(f1_lengths), 2), round(np.std(ferrari_lengths), 2), round(np.std(lambo_lengths), 2), round(np.std(leeuw_lengths), 2), round(np.std(mondriaan_1_lengths), 2), round(np.std(mondriaan_2_lengths), 2), round(np.std(mondriaan_3_lengths), 2), round(np.std(mondriaan_4_lengths), 2), round(np.std(mondriaan_5_lengths), 2), round(np.std(pug_lengths), 2)]
mean_val = [round(np.mean(aston_lengths), 2), round(np.mean(cat_lengths), 2), round(np.mean(dog_lengths), 2), round(np.mean(elephant_lengths), 2), round(np.mean(f1_lengths), 2), round(np.mean(ferrari_lengths), 2), round(np.mean(lambo_lengths), 2), round(np.mean(leeuw_lengths), 2), round(np.mean(mondriaan_1_lengths), 2), round(np.mean(mondriaan_2_lengths), 2), round(np.mean(mondriaan_3_lengths), 2), round(np.mean(mondriaan_4_lengths), 2), round(np.mean(mondriaan_5_lengths), 2), round(np.mean(pug_lengths), 2)]

for mu, std in zip(mean_val, std_val):
    if std == 0:
        std = 100
    # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
    probabilities = norm.pdf(domain, mu, std)
    plt.plot(domain, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")

plt.legend(loc=9, bbox_to_anchor=(0.25, 1), ncol=2)
plt.xlabel("length")
plt.ylabel("Probability")
plt.show()
