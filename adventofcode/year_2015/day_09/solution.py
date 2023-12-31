from adventofcode.utils import solve

import itertools


def add_distance(distances: dict, location_1: str, location_2: str, distance: int) -> None:
    if location_1 not in distances:
        distances[location_1] = dict()
    distances[location_1][location_2] = distance


def initialize_distances(inp: str) -> str:
    locations = set()
    distances = dict()
    for input_line in inp.splitlines():
        location_1 = input_line.split()[0]
        location_2 = input_line.split()[2]
        distance = int(input_line.split()[4])

        locations.add(location_1)
        locations.add(location_2)
        add_distance(distances, location_1, location_2, distance)
        add_distance(distances, location_2, location_1, distance)
    return locations, distances


def solve_riddle(inp: str, comparison):
    locations, distances = initialize_distances(inp)
    permutations = set(itertools.permutations(locations, len(locations)))
    result = None
    for permutation in permutations:
        distance = 0
        for i in range(len(locations) - 1):
            distance += distances[permutation[i]][permutation[i+1]]
        result = distance if result is None else comparison(result, distance)
    return result


def solve_part_i(inp: str, debug: bool = False):
    return solve_riddle(inp, min)


def solve_part_ii(inp: str, debug: bool = False):
    return solve_riddle(inp, max)


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=[605], debug=False)
solve(part=None, solver=solve_part_ii, test_prefix="test_", test_expected_results=[982], debug=False)
