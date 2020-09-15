# this quick script only renames the files for the dataset.
import os

for file in os.listdir("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/mixtures"):
    cleaned_name = file.replace(".wav","")

    intfile = int(cleaned_name)

    os.rename("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/mixtures/"+file, "/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/dataset/mixtures/{:02d}_amzn_mix.wav".format(intfile))

