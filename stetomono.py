# # # ffmpeg -i stereo.wav -map_channel 0.0.0 left.wav -map_channel 0.0.1 right.wav
# # import os.system
# # subprocess.run(["ls", "-l"])
import os
def to_mono():
    p = os.popen('ffmpeg -i stutter.wav -map_channel 0.0.0 final.wav')
    print(p.read())
    return 1