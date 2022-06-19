
#for files in the folder
import os
import subprocess

#loop through sub-directory in order to get all files


# loop through the files in the folder
print(os.getcwd())

#open txtfile
outputfile = open("output_TSPRES.txt", "w")
for directory  in os.listdir(os.getcwd()):
#check if file is directory
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                bmpfilename = filename.replace(".txt", ".bmp")
                tmp = subprocess.run(["D:\\Users\\Stephan\\Documents\\GitHub\\R2D2KLASB\\Research\\CalculateSteps.exe", directory + "\\" + filename, directory+ '\\' + bmpfilename], stdout=subprocess.PIPE)
                print(directory + "\\" + filename + "\t" + tmp.stdout.decode('utf-8'))
                outputfile.write(directory + "\\" + filename + tmp.stdout.decode('utf-8') + "\n")

outputfile.close()
