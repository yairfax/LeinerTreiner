# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_taam(given, expected, base, syll):
#df=pd.DataFrame({'x': range(1,10), 'y': np.random.randn(9)*80+range(1,10) })

    df=pd.DataFrame({'x': [i for i in range(1, len(expected)+1)], 
                        'Expected': expected, 'Given': given})
    #d = {'col1': [1, 2], 'col2': [3, 4]}
    #  df = pd.DataFrame(data=d)
    # plot
    
    #palette = plt.get_cmap('Set1')
    #palette = ['k', 'r']

    #num = 0
    #for col in df.drop('x', axis=1):
      #  num += 1
        #plt.plot( 'x', 'y', data=df, linestyle='-', marker='x')
       # plt.plot(df['x'], df[col], marker='o', color=palette[num], linestyle='-', 
            #    linewidth=2, alpha=0.9, label=col, markersize=15)
    
    plt.figure()
    plt.plot(df['x'], df['Expected'], marker='o', color='k', linestyle='-', 
            linewidth=2, alpha=0.9, label='Expected', markersize=15)
    plt.plot(df['x'], df['Given'], marker='o', color='r', linestyle='-', 
            linewidth=2, alpha=0.9, label='Given', markersize=15)
                                    
    plt.legend(loc=0, ncol = 2)
    plt.xticks(range(1, len(expected)+1), syll)
    
    min_note = min(np.amin(expected), np.amin(given))
    max_note = max(np.amax(expected), np.amax(given))
    plt.ylim(min_note, max_note)
    
    bottom, top = plt.ylim()
    bottom = int(bottom)
    top = int(top)
    notes = [
        'C2', 'C2#', 'D2', 'D2#', 'E2', 'F2', 'F2#', 'G2', 'G2#', 'A2', 'A2#', 'B2',
        'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3',
        'C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#', 'A4', 'A4#', 'B4',
        'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#', 'A5', 'A5#', 'B5']
    
    start_key = notes.index(base)
    
    plt.yticks([i for i in range(bottom, top + 1)], 
                notes[(start_key + min_note):(start_key + max_note + 1)])
    plt.show()

