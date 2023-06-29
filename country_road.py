"""
There is an old country road that runs around a lake. Along the road are six cottages.
Two of the cottages are located one mile apart. Two of the cottages are located two miles
apart. Two of the cottages are located three miles apart and so on...
"""

import itertools as it
from typing import Iterable
from rich import print
from more_itertools import subslices

ROAD_LENGTH = 27
COTTAGES = 6


def _calc_cottage_distances(locations: Iterable) -> tuple[int]:
    pairwise_distances = tuple(y - x for x, y in it.pairwise(locations))
    last_to_first_distance = (ROAD_LENGTH - locations[-1],)
    return pairwise_distances + last_to_first_distance


def _contains_integral_values_to_13(distances: tuple) -> bool:
    integral_distances = set(
        sum(s) % ROAD_LENGTH for s in subslices(distances + distances)
    )
    return len(integral_distances) == ROAD_LENGTH


if __name__ == "__main__":
    possibile_locations = (
        _calc_cottage_distances(c)
        for c in it.combinations(range(0, ROAD_LENGTH), COTTAGES)
        if sum(_calc_cottage_distances(c)) == ROAD_LENGTH
    )
    solutions = []
    seen = []
    for distances in possibile_locations:
        if _contains_integral_values_to_13(distances) and sorted(distances) not in seen:
            solutions.append(distances)
            seen.append(sorted(distances))
    print(solutions)
