
#for files in the folder
import os
import subprocess

#loop through sub-directory in order to get all files


# loop through the files in the folder
print(os.getcwd())
cur_dir = os.getcwd()
#open txtfile
outputfile = open("output_ORIGINAL_STEPS.txt", "w")
for filename  in os.listdir(os.getcwd()):
#check if file is directory
    print(filename)
    if filename.endswith(".txt") and filename != "logfile.txt" and not filename.startswith("output_ORIGINAL"):
        bmpfilename = filename.replace(".txt", ".bmp")
        tmp = subprocess.run(["D:\\Users\\Stephan\\Documents\\GitHub\\R2D2KLASB\\Research\\CalculateSteps.exe", cur_dir + "\\" + filename, cur_dir+ '\\' + bmpfilename], stdout=subprocess.PIPE)
        print(tmp.stdout.decode('utf-8'))
        outputfile.write(filename + " " + tmp.stdout.decode('utf-8') + "\n")

outputfile.close()