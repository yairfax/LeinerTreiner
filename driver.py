import argparse
from analyze import *

parser = argparse.ArgumentParser()
parser.add_argument('--trop', '-t', type=str, required=True)

args = parser.parse_args()

print(parse('test.m4a'))