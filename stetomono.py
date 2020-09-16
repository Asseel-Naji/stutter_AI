# # ffmpeg -i stereo.wav -map_channel 0.0.0 left.wav -map_channel 0.0.1 right.wav
# import os.system
# subprocess.run(["ls", "-l"])
import os

p = os.popen('ffmpeg -i /home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/test.wav -map_channel 0.0.0 /home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/left.wav -map_channel 0.0.1 /home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/right.wav')
print(p.read())