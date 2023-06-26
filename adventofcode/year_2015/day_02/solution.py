from adventofcode.utils import solve


def solve_part_i(inp:str, **kwargs):
    total = 0

    for box in inp.splitlines():
        h, w, l = map(int, box.split("x"))
        side_a, side_b, side_c = h * w, h * l, w * l
        total += 2 * (side_a + side_b + side_c) + min(side_a, side_b, side_c)

    return total


def solve_part_ii(inp:str, **kwargs):
    total = 0

    for box in inp.splitlines():
        h, w, l = map(int, box.split("x"))
        total += 2 * (h + w + l - max(h, w, l)) + h * w * l

    return total


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=[58, 43])
solve(part=None, solver=solve_part_ii, test_prefix="test_", test_expected_results=[34, 14])
