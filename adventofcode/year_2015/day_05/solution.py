from adventofcode.utils import solve

import re


def has_duplicated_pair_check(word: str, debug: bool = False):
    for i in range(len(word) - 3):
        if word[i:i+2] in word[i+2:]:
            if debug:
                print(f"\tDuplicated pair: {word[i:i+2]}")
            return True
    return False


def has_shifted_duplicate_check(word: str):
    for i in range(len(word) - 2):
        if word[i+2] == word[i]:
            return True
    return False


def solve_part_i(inp: str, debug: bool = False):
    nice_words_cnt = 0
    for word in inp.splitlines():
        has_vowels = len(re.findall("[aeiou]", word)) > 2
        has_duplicated_element = len(re.findall(r"((\S)\2{1,})", word)) > 0
        has_blacklisted_elements = len(re.findall("(ab)|(cd)|(pq)|(xy)", word)) > 0
        if debug:
            print(f"\tWord: {word}, "
                  f"has at least three vowels: {has_vowels}, "
                  f"has duplicated letter: {has_duplicated_element}, "
                  f"blacklisted element: {has_blacklisted_elements}")
        if has_vowels and has_duplicated_element and not has_blacklisted_elements:
            nice_words_cnt += 1
    return nice_words_cnt


def solve_part_ii(inp: str, debug: bool = False):
    nice_words_cnt = 0
    for word in inp.splitlines():
        has_duplicated_pair = has_duplicated_pair_check(word, debug)
        has_shifted_duplicate = has_shifted_duplicate_check(word)
        if debug:
            print(f"\tWord: {word}, "
                  f"has duplicated pair: {has_duplicated_pair}, "
                  f"has shifted duplicate: {has_shifted_duplicate}")
        if has_duplicated_pair and has_shifted_duplicate:
            nice_words_cnt += 1
    return nice_words_cnt


solve(part=None, solver=solve_part_i, test_prefix="test_01_", test_expected_results=[1, 1, 0, 0, 0], debug=False)
solve(part=None, solver=solve_part_ii, test_prefix="test_02_", test_expected_results=[1, 1, 0, 0], debug=False)
