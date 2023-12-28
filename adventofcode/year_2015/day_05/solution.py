from adventofcode.utils import solve

import re


def has_duplicated_pair(word: str, debug: bool = False):
    for i in range(len(word) - 3):
        if word[i:i+2] in word[i+2:]:
            if debug:
                print(f"\tDuplicated pair: {word[i:i+2]}")
            return True
    return False


def has_shifted_duplicate(word: str):
    for i in range(len(word) - 2):
        if word[i+2] == word[i]:
            return True
    return False


def solve_part_i(inp: str, debug: bool = False):
    nice_words_cnt = 0
    for word in inp.splitlines():
        vowels = len(re.findall("[aeiou]", word)) > 2
        duplicate = len(re.findall(r"((\S)\2{1,})", word)) > 0
        blacklisted = len(re.findall("(ab)|(cd)|(pq)|(xy)", word)) > 0
        if debug:
            print(f"\tWord: {word}, "
                  f"has at least three vowels: {vowels}, "
                  f"has duplicated letter: {duplicate}, "
                  f"blacklisted element: {blacklisted}")
        if vowels and duplicate and not blacklisted:
            nice_words_cnt += 1
    return nice_words_cnt


def solve_part_ii(inp: str, debug: bool = False):
    nice_words_cnt = 0
    for word in inp.splitlines():
        duplicated_pair = has_duplicated_pair(word, debug)
        shifted_duplicate = has_shifted_duplicate(word)
        if debug:
            print(f"\tWord: {word}, "
                  f"has duplicated pair: {duplicated_pair}, "
                  f"has shifted duplicate: {shifted_duplicate}")
        if duplicated_pair and shifted_duplicate:
            nice_words_cnt += 1
    return nice_words_cnt

solve(part=None, solver=solve_part_i, test_prefix="test_01_", test_expected_results=[1, 1, 0, 0, 0], debug=False)
solve(part=None, solver=solve_part_ii, test_prefix="test_02_", test_expected_results=[1, 1, 0, 0], debug=False)
