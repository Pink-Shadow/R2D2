#for files in the folder
import os
import subprocess

#loop through sub-directory in order to get all files


# loop through the files in the folder
print(os.getcwd())

#open txtfile
outputfile = open("output_ORIGINAL.txt", "w")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt") and filename != "output_ORIGINAL.txt":
        bmpfilename = filename.replace(".txt", ".bmp")
        tmp = subprocess.run(["D:\\Users\\Stephan\\Documents\\GitHub\\R2D2KLASB\\Research\\CalculateSteps.exe", filename, bmpfilename], stdout=subprocess.PIPE)
        print(filename + "\t" + tmp.stdout.decode('utf-8'))
        outputfile.write(filename + " " + tmp.stdout.decode('utf-8') + "\n")

outputfile.close()
