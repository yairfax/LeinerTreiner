import numpy as np
from taamim_torah import *

def get_notes(taamim):
    notes = []
    timing = []
    pronunc = []
    for taam in taamim:
        notes += trop_notes[taam]
        notes += [np.nan]

        timing += [1 for i in range(len(trop_notes[taam]))]
        timing += [1]

        pronunc += trop_name[taam]
        pronunc += [""]
    
    notes = notes[:-2]
    timing = [i for i in range(len(timing))]
    timing = timing[:-2]
    timing = [i/len(timing) for i in timing]
    pronunc = pronunc[:-2]

    return notes, timing, pronunc