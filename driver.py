import argparse
from itertools import groupby
from analyze import *
from plotter import *
from taamim_torah import *
from utils import *
from aubio import midi2note

parser = argparse.ArgumentParser()
parser.add_argument('--trop', '-t', type=str, required=True, nargs="+")

args = parser.parse_args()

given = extract_notes_from_file(0, 'test2.m4a')

offset = given[0] - trop_notes['munach-munach-rvii'][0]
given_transpose = [i - offset for i in given]

expected_notes, expected_timing, pronunc = get_notes(['munach-munach-rvii', 'munach-rvii', 'rvii'])

print(expected_notes)
print(expected_timing)
print(pronunc)

plot_taam(expected_notes, expected_timing, given_transpose, midi2note(given[0]), pronunc)

# print(a)
# print([i[0] for i in groupby(a)])