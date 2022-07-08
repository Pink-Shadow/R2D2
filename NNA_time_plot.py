import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename_tijd =[["aston.txt", 1.4842777013778687],
                ["cat.txt", 10.325533413887024],
                ["dog.txt", 18.796085953712463],
                ["elephant.txt", 42.47500519752502],
                ["f1.txt", 7.056083798408508],
                ["ferrari.txt", 2.6067909240722655],
                ["lambo.txt", 2.1178187847137453],
                ["leeuw.txt", 50.69488701820374],
                ["mondriaan_1.txt", 0.031006360054016115],
                ["mondriaan_2.txt", 2.7649765253067016],
                ["mondriaan_3.txt", 3.498494338989258],
                ["mondriaan_4.txt", 44.46061313152313],
                ["mondriaan_5.txt", 14.679688549041748],
                ["pauw.txt", 144.00858836174012],
                ["pug.txt", 34.56406393051147]]
                    
    filenames = []
    times = []
    objects_filename = {}

    for i in filename_tijd:
        filenames.append(i[0])

    with open("./PYTHON_TSP/objects.txt", "r") as f:
        for line in f:
            line = line.split(" ")
            for i, name in enumerate(filenames):
                if name == line[0]:
                    objects_filename[int(line[2])] = str(line[0][:-4])
                    filenames.pop(i)

        sorted = sorted(objects_filename.items())

        names = []
        for key, value in sorted:
            names.append(str(key) + "\n" + str(value))
            for i, name in enumerate(filename_tijd):
                print(name, value)
                if name[0] == value+".txt":
                    times.append(name[1])

    plt.ylabel("Time in seconds")
    plt.xlabel("Objects per file")
    plt.bar(names,times)
    plt.savefig('NNA_times.png')
    plt.show()
    