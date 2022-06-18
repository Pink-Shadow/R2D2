import TSP
import os


for file_name in os.listdir("./original")[:len(os.listdir("./original"))//2]:
    print(file_name)
    coords = TSP.parse_gcode("./original/" + file_name)
    optimized = TSP.run(coords)
    TSP.write_route_gcode_to_file(optimized, "./TSP/A/"+file_name)

