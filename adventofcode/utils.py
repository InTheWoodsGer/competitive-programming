import glob


def solve(
        part:str,
        solver: callable,
        test_prefix: str,
        test_expected_results: list,
        debug:bool = False):

    if test_prefix and test_expected_results:
        test_cases = glob.glob(f"./{test_prefix}*")
        if len(test_cases) != len(test_expected_results):
            raise Exception(f"Number of test cases and expected results are different!")

        test_failure = False
        for i, test_case in enumerate(sorted(test_cases)):
            print(f"Executing test case: {test_case}")
            with open(test_case, "r") as f:
                test_case = f.read()

            test_case_result = solver(test_case, debug=debug)
            print(f"\tExpected result: {test_expected_results[i]}, actual result: {test_case_result}")
            if test_case_result != test_expected_results[i]:
                test_failure = True

        if test_failure:
            raise Exception("Test cases failed")

    print("Executing on my input")
    my_input_filename = f"my_input{f'_{part}' if part else ''}.txt"
    with open(my_input_filename, "r") as f:
        my_input = f.read()

    print(f"\tThe result for my input: {solver(my_input, debug=debug)}\n")