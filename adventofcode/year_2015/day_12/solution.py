from adventofcode.utils import solve

import json


def has_red_value(element):
    return len([v for v in element.values() if isinstance(v, str) and v == "red"]) > 0


def element_handler(element, ignore_reds: bool):
    numbers_sum = 0
    if isinstance(element, list):
        for item in element:
            numbers_sum += element_handler(item, ignore_reds)
    elif isinstance(element, dict):
        if ignore_reds or not has_red_value(element):
            for item in element.values():
                numbers_sum += element_handler(item, ignore_reds)
    elif isinstance(element, int):
        return int(element)

    return numbers_sum


def solve_part_i(inp: str, debug: bool = False):
    return element_handler(json.loads(inp), True)


def solve_part_ii(inp: str, debug: bool = False):
    return element_handler(json.loads(inp), False)


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=[6, 3, 0, 0, 0, 0, 6, 3], debug=True)
solve(part=None, solver=solve_part_ii, test_prefix="test_", test_expected_results=[6, 3, 0, 0, 0, 0, 6, 3], debug=False)
