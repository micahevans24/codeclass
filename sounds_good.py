# CS5 Gold, Lab 4
# Filename: hw4pr1.py
# Name:
# Problem description: Lab 4 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed in 2015
# if you are having trouble, comment out the above line...




# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC



# Function to write #1:  scale







# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC



# Function to write #2:  add_2






# Function to write #3:  add_3






# Function to write #4:  add_scale_2








# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x






# Function to write #5:  replace_some











#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    sound_data = [0, 0]           # an "empty" list
    read_wav(filename, sound_data)# get data INTO sound_data

    samps = sound_data[0]         # the raw pressure samples

    print("The first 10 sound-pressure samples are\n", samps[:10])
    sr = sound_data[1]            # the sampling rate, sr

    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsamps = samps                     # same samples as before
    new_sound_data = [newsamps, newsr]   # new sound data pair
    write_wav(new_sound_data, "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'



def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #1:  reverse







# Sound function to write #2:  volume







# Sound function to write #3:  static







# Sound function to write #4:  overlay







# Sound function to write #5:  echo








# Helper function for generating pure tones
def gen_pure_tone(freq, seconds, sound_data):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    if sound_data != [0, 0]:
        print("Please proivde a value of [0, 0] for sound_data.")
        return
    sampling_rate = 22050
    # how many data samples to create
    nsamples = int(seconds*sampling_rate) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sampling_rate   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    sound_data[0] = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    sound_data = [0, 0]
    gen_pure_tone(freq, time_in_seconds, sound_data)

    print("Writing out the sound data...")
    write_wav(sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #6:  chord

