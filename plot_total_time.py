import matplotlib.pyplot as plt
import numpy as np

totalTimesTSP = {
    "aston" : {
        "time" : 264
    },
    "cat" : {
        "time" : 807
    },
    "dog" : {
        "time" : 988
    },
    "elephant" : {
        "time" : 1222
    },
    "f1" : {
        "time" : 468
    },
    "ferrari" : {
        "time" : 296
    },
    "lambo" : {
        "time" : 298
    },
    "leeuw" : {
        "time" : 2049
    },
    "mondriaan_1" : {
        "time" : 73
    },
    "mondriaan_2" : {
        "time" : 561
    },
    "mondriaan_3" : {
        "time" : 444
    },
    "mondriaan_4" : {
        "time" : 1190
    },
    "mondriaan_5" : {
        "time" : 838
    },
    "pauw" : {
        "time" : 3059
    },
    "pug" : {
        "time" : 1411
    }
}

totalTimesNNA = {
    "aston" : {
        "time" : 217
    },
    "cat" : {
        "time" : 584
    },
    "dog" : {
        "time" : 775
    },
    "elephant" : {
        "time" : 872
    },
    "f1" : {
        "time" : 356
    },
    "ferrari" : {
        "time" : 241
    },
    "lambo" : {
        "time" : 245
    },
    "leeuw" : {
        "time" : 1292
    },
    "mondriaan_1" : {
        "time" : 58
    },
    "mondriaan_2" : {
        "time" : 364
    },
    "mondriaan_3" : {
        "time" : 308
    },
    "mondriaan_4" : {
        "time" : 862
    },
    "mondriaan_5" : {
        "time" : 530
    },
    "pauw" : {
        "time" : 1768
    },
    "pug" : {
        "time" : 913
    }
}

totalTimesOriginal = {
    "aston" : {
        "time" : 286
    },
    "cat" : {
        "time" : 820
    },
    "dog" : {
        "time" : 1077
    },
    "elephant" : {
        "time" : 1281
    },
    "f1" : {
        "time" : 432
    },
    "ferrari" : {
        "time" : 309
    },
    "lambo" : {
        "time" : 304
    },
    "leeuw" : {
        "time" : 1857
    },
    "mondriaan_1" : {
        "time" : 73
    },
    "mondriaan_2" : {
        "time" : 454
    },
    "mondriaan_3" : {
        "time" : 486
    },
    "mondriaan_4" : {
        "time" : 1341
    },
    "mondriaan_5" : {
        "time" : 881
    },
    "pauw" : {
        "time" : 2959
    },
    "pug" : {
        "time" : 1303
    }
}

filenames = []
times = []
objects_filename = {}

for name,value in totalTimesTSP.items():
    filenames.append(name)

with open("./PYTHON_TSP/objects.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        for i, name in enumerate(filenames):
            if name+".txt" == line[0]:
                objects_filename[int(line[2])] = str(line[0][:-4])
                filenames.pop(i)

    sorted = sorted(objects_filename.items())


tijdenTSP = [totalTimesTSP[y]["time"] for x,y in sorted]
tijdenNNA = [totalTimesNNA[y]["time"] for x,y in sorted]
tijdenOriginal = [totalTimesOriginal[y]["time"] for x,y in sorted]
names = []
for i in sorted:
    names.append( str(i[0]) + "\n" + i[1])


X_axis = np.arange(len(names))

plt.bar(X_axis - 0.2, tijdenOriginal, 0.2, label = 'Original')
plt.bar(X_axis, tijdenNNA, 0.2, label = 'NNA')
plt.bar(X_axis + 0.2, tijdenTSP, 0.2, label = 'TSP')

plt.xticks(X_axis, names)
plt.ylabel("Total time in seconds")
plt.xlabel("Objects per file")
plt.legend()
plt.show()
