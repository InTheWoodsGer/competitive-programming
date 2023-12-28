from adventofcode.utils import solve
import hashlib


def solve_problem(inp: str, expected_prefix: str, debug: bool = False):
    num = 1
    while not hashlib.md5((inp + str(num)).encode()).hexdigest().startswith(expected_prefix):
        if debug and num % 1000 == 0:
            print(f"Number: {num}, md5: {hashlib.md5((inp + str(num)).encode()).hexdigest()}")
        num += 1
    return num


def solve_part_i(inp: str, debug: bool = False):
    return solve_problem(inp, "00000", debug)


def solve_part_ii(inp: str, debug: bool = False):
    return solve_problem(inp, "000000", debug)


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=[609043, 1048970])
solve(part=None, solver=solve_part_ii, test_prefix=None, test_expected_results=None)
