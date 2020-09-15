# who got time to fix  the names manually?
import os

for file in os.listdir("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/instruments"):
    fixed_name = file.replace("mix.wav","inst.wav")


    os.rename("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/instruments/"+file, "/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/instruments/"+fixed_name)

