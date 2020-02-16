import argparse
from itertools import groupby
import sys
from aubio import midi2note
from analyze import *
# from plotter import *
from taamim_torah import *
from utils import *
from play import *

parser = argparse.ArgumentParser()
parser.add_argument('--taam', '-t', type=str, required=True, nargs="+", help="""
Sequence of t'amim to be played. Options are:
    %s.
Note that the symbols for different munachim include
the t'amim that follow them for the sake of differentiation,
but the actual taam is still just a munach. For example,
'munach-rvii' is the just the munach preceding a rvii, and
'munach-munach-rvii' is the taam preceding that.
Note also that it is up to the user to input t'amim that make
sense in sequence. For example, the sequence 'munach-munach-rvii' 'tlisha-gdola'
would not be found anywhere in Torah, but our program
doesn't differentiate that.
""" % str(trop))

args = parser.parse_args()

given_taamim = args.taam
for taam in given_taamim:
    if taam not in trop:
        print("Taam '%s' not found" % taam)
        sys.exit(1)

given = extract_notes_from_file(0, 'test2.m4a')

offset = given[0] - trop_notes[given_taamim[0]][0]
given_transpose = [i - offset for i in given]

expected_notes, expected_timing, pronunc = get_notes(given_taamim)

transposed_expected = [i + 70 for i in expected_notes]

play_taam(transposed_expected)

# print(expected_timing)

# changed_times = grad_descent(given_transpose, np.linspace(0, 1, len(given_transpose)), expected_notes, expected_timing)
changed_times = np.linspace(0, 1, len(given_transpose))

# print(changed_times)
# print(np.linspace(0, 1, len(given)))

# plot_taam(expected_notes, expected_timing, given_transpose, changed_times, midi2note(given[0]), pronunc)
