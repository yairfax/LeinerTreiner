# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_taam(expected, expected_timing, given, base, syll):
    plt.figure()

    plt.plot(expected_timing, expected, marker='o', color='k', linestyle='-', 
            linewidth=2, alpha=0.9, label='Expected', markersize=10)
    plt.plot(np.linspace(0, 1, len(given)), given, marker='o', color='r', linestyle='-', 
            linewidth=2, alpha=0.9, label='Given', markersize=5)
                                    
    plt.legend(loc=0, ncol = 2)
    plt.xticks(np.linspace(0, 1, len(syll)), syll)
    
    min_note = int(min(np.nanmin(expected), np.nanmin(given)))
    max_note = int(max(np.nanmax(expected), np.nanmax(given)))

    
    bottom, top = plt.ylim()
    bottom = int(bottom)
    top = int(top)
    notes = [
        'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
        'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
        'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
        'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']
    
    start_key = notes.index(base)
    
    plt.yticks([i for i in range(bottom, top + 1)], 
                notes[(start_key + min_note):(start_key + max_note + 1)])
    plt.show()

