import time
from aubio import miditofreq
from pysine import sine
import numpy as np

def play_taam(seq):
    for taam in seq:
        print(taam)
        if taam != np.nan:
            freq = miditofreq(taam)
            sine(frequency=freq, duration=.3)
        else:
            time.sleep(.3)