from adventofcode.utils import solve


def solve_part_i(inp, **kwargs):
    return inp.count("(") - inp.count(")")


def solve_part_ii(inp, debug):
    cnt = 0
    floor = 0
    while floor != -1:
        floor += 1 * (1 if inp[cnt:cnt+1] == "(" else -1)
        cnt += 1
        if debug:
            print(f"   Step: {cnt}, order: {inp[cnt:cnt + 1]}, new floor: {floor}")
    return cnt


solve(part=None, solver=solve_part_i, test_prefix="test_01_", test_expected_results=[0, 0, 3, 3, 3, -1, -1, -3, -3])
solve(part=None, solver=solve_part_ii, test_prefix="test_02_", test_expected_results=[1, 5])
