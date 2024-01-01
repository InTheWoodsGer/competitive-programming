from adventofcode.utils import solve

import string
import re

ALL_LETTERS = list(string.ascii_lowercase)
THREE_LETTER_INCREASES = ["".join(list(ALL_LETTERS)[i:i + 3]) for i in range(len(list(ALL_LETTERS)) - 2)]

BLACKLISTED_LETTER_FOLLOW_UPS = {"i": "j", "o": "p", "l": "m"}
BLACKLISTED_LETTERS = set(BLACKLISTED_LETTER_FOLLOW_UPS.keys())

VALID_LETTERS = [letter for letter in ALL_LETTERS if letter not in BLACKLISTED_LETTERS]
VALID_LETTER_FOLLOW_UPS = dict(zip(VALID_LETTERS[:-1], VALID_LETTERS[1:]))


def fix_invalid_letter(password: str, debug: bool = False) -> str:
    password_length = len(password)
    for i in range(password_length):
        if password[i] in BLACKLISTED_LETTERS:
            password = password[:i] + BLACKLISTED_LETTER_FOLLOW_UPS[password[i]] + ("a" * (password_length-i-1))
            break
    if debug:
        print(f"\tPassword after blacklisted letter check: {password}")

    return password


def contains_three_letter_follow_up(password: str) -> bool:
    return len([i for i in THREE_LETTER_INCREASES if i in password]) > 0


def contains_triplet(password: str) -> bool:
    return len(re.findall(r"((\S)\2{2,})", password)) > 0


def contains_at_least_two_different_duplicates(password: str) -> bool:
    return len(set(re.findall(r"((\S)\2{1,})", password))) > 1


def is_valid_password(password: str) -> bool:
    if not contains_three_letter_follow_up(password):
        return False
    if contains_triplet(password):
        return False
    if not contains_at_least_two_different_duplicates(password):
        return False
    return True


def solve_riddle(password: str, debug: bool = False) -> str:
    if debug:
        print(f"\tOriginal password: {password}")

    password = fix_invalid_letter(password, debug)
    password_last_index = len(password) - 1
    while True:
        for i in range(len(password)):
            if password[password_last_index-i] == "z":
                password = password[0:password_last_index-i] + "a" + password[password_last_index-i+1:]
            else:
                password = password[0:password_last_index-i]\
                           + VALID_LETTER_FOLLOW_UPS[password[password_last_index-i]]\
                           + password[password_last_index-i+1:]
                break

        if is_valid_password(password):
            return password
    raise Exception("New password not found!")


def solve_part_i(password: str, debug: bool = False):
    return solve_riddle(password, debug)


def solve_part_ii(password: str, debug: bool = False):
    new_password = solve_riddle(password, debug)
    return solve_riddle(new_password, debug)


solve(part=None, solver=solve_part_i, test_prefix="test_", test_expected_results=["abcdffaa", "ghjaabcc"], debug=True)
solve(part=None, solver=solve_part_ii, test_prefix="test_", test_expected_results=["abcdffbb", "ghjbbcdd"], debug=False)
