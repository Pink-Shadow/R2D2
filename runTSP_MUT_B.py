import TSP_mut_custom as TSP
import os

for i in range(1, 21):
    try:
        os.mkdir("./TSP_MUT/B/round_" + str(i))
    except FileExistsError:
        pass
    
    print(f"ROUND {i} TSP_MUT B")
    for file_name in os.listdir("./original")[len(os.listdir("./original"))//2:]:
        print(f"file: {file_name}'s {i}'th time")
        coords = TSP.parse_gcode("./original/" + file_name)
        shortest_route, shortest_dist, iterations = TSP.run(coords)
        TSP.write_route_gcode_to_file(shortest_route, f"./TSP_MUT/B/round_{i}/{file_name}")
        with open("./TSP_MUT/B/meta_data.txt", "a") as file:
            file.write(f"{file_name} dist {shortest_dist} iterations {iterations}\n")
