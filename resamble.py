#I officially GIVE UP ON THIS FUNCTION.
# In order to remove silence I have to split into mono, then resample and then clean
# and EVEN AFTER I managed to do all that, the script I use to remove silence doesn't like
# libosa resambling, however when I manually resamble with audacity it works just fine.
# THIS MAKES NO SENSE WHATSOEVER.

# I THOUGHT THIS WILL BE AN EASY TASK AND NOW I WASTED 3 HOURS!


# import librosa
# import resampy
# import wave
# import scipy
# x, sr_orig = librosa.load("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/right.wav",sr=None)
# y_low = resampy.resample(x, sr_orig, 16000)
# scipy.io.wavfile.write("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/ugh.wav", 16000, y_low)
# # librosa.output.write_wav("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/librosad.wav",y,sr,True)


# # import os
# # import wave

# # def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
# #     if not os.path.exists(src):
# #         print('Source not found!')
# #         return False

# #     if not os.path.exists(os.path.dirname(dst)):
# #         os.makedirs(os.path.dirname(dst))

# #     try:
# #         s_read = wave.open(src, 'r')
# #         s_write = wave.open(dst, 'w')
# #     except:
# #         print('Failed to open files!')
# #         return False

# #     n_frames = s_read.getnframes()
# #     data = s_read.readframes(n_frames)

# #     try:
# #         converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
# #         if outchannels == 1:
# #             converted = audioop.tomono(converted[0], 2, 1, 0)
# #     except:
# #         print('Failed to downsample wav')
# #         return False

# #     try:
# #         s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
# #         s_write.writeframes(converted)
# #     except:
# #         print('Failed to write wav')
# #         return False

# #     try:
# #         s_read.close()
# #         s_write.close()
# #     except:
# #         print('Failed to close wav files')
# #         return False

# #     return True
# # downsampleWav("/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/test.wav","/home/ravingmad/Desktop/Work/amazonthon/stutter_AI/silence_removal_trials/downed.wav")