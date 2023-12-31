from adventofcode.utils import solve


def solve_riddle(inp: str, rounds: int, debug: bool = False):
    word = inp
    for i in range(rounds):
        new_word, current_digit, digit_cnt = "", None, 0
        for digit in word:
            if current_digit is None:
                current_digit = digit
            elif current_digit is not None and current_digit != digit:
                new_word += str(digit_cnt) + current_digit
                current_digit = digit
                digit_cnt = 0
            digit_cnt += 1
        new_word += str(digit_cnt) + current_digit
        word = new_word
        if debug:
            print(word)

    return len(word)


def solve_tester_i(inp: str, debug: bool = False):
    return solve_riddle(inp, 1, debug)


def solve_tester_ii(inp: str, debug: bool = False):
    return solve_riddle(inp, 5, debug)


def solve_part_i(inp: str, debug: bool = False):
    return solve_riddle(inp, 40, debug)


def solve_part_ii(inp: str, debug: bool = False):
    return solve_riddle(inp, 50, debug)


solve(part=None, solver=solve_tester_i, test_prefix="test_01", test_expected_results=[2, 2, 4, 6, 6], debug=False)
solve(part=None, solver=solve_tester_ii, test_prefix="test_02", test_expected_results=[6], debug=False)
solve(part=None, solver=solve_part_i, test_prefix=None, test_expected_results=None, debug=False)
solve(part=None, solver=solve_part_ii, test_prefix=None, test_expected_results=None, debug=False)
