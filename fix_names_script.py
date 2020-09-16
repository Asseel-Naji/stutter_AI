# who got time to fix  the names manually?
import os

for file in os.listdir("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/stutters"):
    fixed_name = file.replace("inst.wav","sttr.wav")


    os.rename("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/stutters/"+file, "/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/stutters/"+fixed_name)

