import numpy as np
import re


def get_all_step_data_TSP():
    data = {

    }
    with open("./PYTHON_TSP/output_TSP_PYTHON.txt") as file:
        for line in file:
            line = line.strip()
            line = line.replace("_", " ").replace(".", " ")
            line = line.split(" ")
            if f"{line[1]}" == "mondriaan":
                line[1] = "mondriaan_{}".format(line[2])
            if f"{line[1]}" in data:
                data[line[1]].append((int(line[-1]), str(f"{line[0]}_{line[1]}.txt")))

            else:
                data[line[1]] = [ (int(line[-1]), str(f"{line[0]}_{line[1]}.txt"))  ]

    return data

def find_nearest(array, value):
    nearest_i = (np.abs(array - value)).argmin()
    return array[nearest_i]

if __name__ == "__main__":
    TSP_data = get_all_step_data_TSP()

    for key, value in TSP_data.items():
        unzipped_list = [[steps for steps, name in value],
                         [name for steps, name in value]]

        mean_steps = np.mean(np.array(unzipped_list[0]))
        nearest_steps = find_nearest(np.array(unzipped_list[0]), mean_steps)
        file_of_nearest_steps = unzipped_list[1][unzipped_list[0].index(nearest_steps)]

        print(f"File closest to the mean amount of steps for image {key}: {file_of_nearest_steps}")