from adventofcode.utils import solve

import itertools


PERSON_ME = "me"


def initialize_input(inp: str) -> dict:
    connections = dict()
    for connection in inp.splitlines():
        person = connection.split()[0]
        next_to = connection.removesuffix(".").split()[-1]
        happiness = int(connection.split()[3])
        happiness *= 1 if connection.split()[2] == "gain" else -1

        if person not in connections:
            connections[person] = dict()
        connections[person][next_to] = happiness
    return connections


def get_happiest_sum(connections, debug):
    if debug:
        print(f"\tConnections: {connections}")

    sitting_orders = list(itertools.permutations(connections.keys()))
    happiest_order = None
    happiest_sum = 0
    for sitting_order in sitting_orders:
        current_happiness_sum = 0
        for i in range(len(sitting_order)):
            left_neighbour = i - 1 if i > 0 else -1
            right_neighbour = i + 1 if i < len(sitting_order) - 1 else 0
            current_happiness_sum += connections[sitting_order[i]][sitting_order[left_neighbour]]
            current_happiness_sum += connections[sitting_order[i]][sitting_order[right_neighbour]]
        if current_happiness_sum > happiest_sum:
            happiest_order = sitting_order
            happiest_sum = current_happiness_sum

    if debug:
        print(f"\t{'-' * 20}")
        print(f"\tHappiest order: {happiest_order}")

    return happiest_sum


def add_myself_to_connections(connections):
    my_connections = dict()
    for person in connections.keys():
        connections[person][PERSON_ME] = 0
        my_connections[person] = 0
    connections[PERSON_ME] = my_connections


def solve_part_i(inp: str, debug: bool = False):
    connections = initialize_input(inp)
    return get_happiest_sum(connections, debug)


def solve_part_ii(inp: str, debug: bool = False):
    connections = initialize_input(inp)
    add_myself_to_connections(connections)
    return get_happiest_sum(connections, debug)


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=[330], debug=True)
solve(part=None, solver=solve_part_ii, test_prefix="test_", test_expected_results=[], debug=False)
