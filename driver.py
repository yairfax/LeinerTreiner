import argparse
from itertools import groupby
from analyze import *
from Plotter import *
from taamim_torah import *

parser = argparse.ArgumentParser()
parser.add_argument('--trop', '-t', type=str, required=True, nargs="+")

args = parser.parse_args()

a = extract_notes_from_file(2, 'mapakh-pashta.m4a')

# plot_taam(trop_notes['shalshelet'], trop_notes['shalshelet'], 'C3', trop_name['shalshelet'])

print(args.trop)

print(a)
print([i[0] for i in groupby(a)])