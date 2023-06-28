"""
There is an old country road that runs around a lake. Along the road are six cottages.
Two of the cottages are located one mile apart. Two of the cottages are located two miles
apart. Two of the cottages are located three miles apart and so on...
"""

import itertools as it
from typing import Iterable
from rich import print
from more_itertools import subslices


def calc_distances(locations: Iterable) -> int:
    return tuple(y - x for x, y in it.pairwise(locations)) + (27 - locations[-1],)


possibile_locations = [
    (c, calc_distances(c))
    for c in it.combinations(range(0, 27), 6)
]


solutions = []
for locations, d in possibile_locations:
    if len(set(sum(s) for s in subslices(d + d) if sum(s) <= 13)) == 13:
        solutions.append((locations, d))

print(set(solutions))
