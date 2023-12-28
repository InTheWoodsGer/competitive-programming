from adventofcode.utils import solve


def initial_lights():
    return [[0 for j in range(1000)] for i in range(1000)]


def get_instruction_details(instruction: str, debug: bool = False):
    instruction = instruction.split()
    if debug:
        print(f"\t{instruction}")
    if instruction[0] == "turn":
        action = instruction[1]
        instruction = instruction[2:]
    else:
        action = instruction[0]
        instruction = instruction[1:]

    from_x = int(instruction[0].split(",")[0])
    from_y = int(instruction[0].split(",")[1])
    to_x = int(instruction[2].split(",")[0])
    to_y = int(instruction[2].split(",")[1])

    return action, from_x, to_x, from_y, to_y


def sum_lights(lights: list):
    summary = 0
    for i in range(1000):
        for j in range(1000):
            summary += lights[i][j]
    return summary


def solve_part_i(inp: str, debug: bool = False):
    lights = initial_lights()

    for instruction in inp.splitlines():
        action, from_x, to_x, from_y, to_y = get_instruction_details(instruction, debug)
        for i in range(from_x, to_x+1):
            for j in range(from_y, to_y+1):
                if action == "on":
                    lights[i][j] = 1
                elif action == "off":
                    lights[i][j] = 0
                else:
                    lights[i][j] = 1 if lights[i][j] == 0 else 0

    return sum_lights(lights)


def solve_part_ii(inp: str, debug: bool = False):
    lights = initial_lights()

    for instruction in inp.splitlines():
        action, from_x, to_x, from_y, to_y = get_instruction_details(instruction, debug)
        for i in range(from_x, to_x+1):
            for j in range(from_y, to_y+1):
                if action == "on":
                    lights[i][j] += 1
                elif action == "off":
                    lights[i][j] = lights[i][j] - 1 if lights[i][j] > 0 else 0
                else:
                    lights[i][j] += 2

    return sum_lights(lights)


solve(part=None, solver=solve_part_i, test_prefix="test_01_", test_expected_results=[1000000, 1000, 999996], debug=False)
solve(part=None, solver=solve_part_ii, test_prefix="test_02_", test_expected_results=[1, 2000000], debug=False)
