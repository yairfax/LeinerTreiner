import argparse
from itertools import groupby
from analyze import *

parser = argparse.ArgumentParser()
parser.add_argument('--trop', '-t', type=str, required=True, nargs="+")

args = parser.parse_args()

a = extract_notes_from_file(2, 'mapakh-pashta.m4a')

print(args.trop)

print(a)
print([i[0] for i in groupby(a)])