from adventofcode.utils import solve


def encode(literal: str) -> str:
    literal = literal.replace("\\", "\\\\")
    literal = literal.replace("\"", "\\\"")
    return literal


def solve_part_i(inp: str, debug: bool = False):
    total_diff = 0
    for literal in inp.splitlines():
        total_diff += (len(literal) - len(eval(literal)))
    return total_diff


def solve_part_ii(inp: str, debug: bool = False):
    total_diff = 0
    for literal in inp.splitlines():
        total_diff += (len(encode(literal)) - len(literal)) + 2
    return total_diff


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=[12], debug=False)
solve(part=None, solver=solve_part_ii, test_prefix="test_", test_expected_results=[19], debug=False)
