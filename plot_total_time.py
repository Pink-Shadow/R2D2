import matplotlib.pyplot as plt

totalTimes = {
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

filenames = []
times = []
objects_filename = {}

for name,value in totalTimes.items():
    filenames.append(name)

with open("./PYTHON_TSP/objects.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        for i, name in enumerate(filenames):
            if name+".txt" == line[0]:
                objects_filename[int(line[2])] = str(line[0][:-4])
                filenames.pop(i)

    sorted = sorted(objects_filename.items())
       

tijden = [totalTimes[y]["time"] for x,y in sorted]
names = []
for i in sorted:
    names.append( str(i[0]) + "\n" + i[1])

plt.ylabel("Total time in seconds")
plt.xlabel("Objects per file")
plt.bar(names , tijden)
plt.savefig('total_times_TSP.png')
plt.show()