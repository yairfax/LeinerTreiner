#plot_taam(given, expected, base_note, name)

from Plotter import *

taam_name = { 'zarka': ['Zar', 'ka', 'a', 'a', 'a', 'a']}
plot_taam([2, 0, -1, 1, -1, -5], [2, 0, -1, -3, -1, -5], "C3", taam_name['zarka'])