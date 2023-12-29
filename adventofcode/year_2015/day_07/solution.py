from adventofcode.utils import solve

KEY_OPERATOR = "OPERATOR"
KEY_VALUE = "VALUE"
KEY_OPERAND, KEY_OPERAND_LEFT, KEY_OPERAND_RIGHT = "OPERAND", "OPERAND_LEFT", "OPERAND_RIGHT"

ASSIGNMENT = "ASSIGNMENT"
GATE_AND, GATE_OR, GATE_NOT, GATE_LSHIFT, GATE_RSHIFT = "AND", "OR", "NOT", "LSHIFT", "RSHIFT"


def initialize_instructions(inp: str):
    instructions = dict()
    for instruction in inp.splitlines():
        if GATE_AND in instruction or GATE_OR in instruction:
            instructions[instruction.split()[4]] = {
                KEY_OPERATOR: instruction.split()[1],
                KEY_VALUE: None,
                KEY_OPERAND_LEFT: instruction.split()[0],
                KEY_OPERAND_RIGHT: instruction.split()[2]
            }
        elif GATE_LSHIFT in instruction or GATE_RSHIFT in instruction:
            instructions[instruction.split()[4]] = {
                KEY_OPERATOR: instruction.split()[1],
                KEY_VALUE: None,
                KEY_OPERAND_LEFT: instruction.split()[0],
                KEY_OPERAND_RIGHT: instruction.split()[2]
            }
        elif GATE_NOT in instruction:
            instructions[instruction.split()[3]] = {
                KEY_OPERATOR: GATE_NOT,
                KEY_VALUE: None,
                KEY_OPERAND: instruction.split()[1]
            }
        else:
            instructions[instruction.split()[2]] = {
                KEY_OPERATOR: ASSIGNMENT,
                KEY_VALUE: None,
                KEY_OPERAND: instruction.split()[0]
            }
    return instructions


def get_value(instructions: dict, wire: str):
    instruction = instructions[wire]

    if instruction[KEY_VALUE] is not None:
        return instruction[KEY_VALUE]

    if instruction[KEY_OPERATOR] == ASSIGNMENT:
        if instruction[KEY_OPERAND].isdigit():
            instruction[KEY_VALUE] = int(instruction[KEY_OPERAND])
        else:
            instruction[KEY_VALUE] = get_value(instructions, instruction[KEY_OPERAND])
    elif instruction[KEY_OPERATOR] == GATE_NOT:
        if instruction[KEY_OPERAND].isdigit():
            instruction[KEY_VALUE] = ~int(instruction[KEY_OPERAND])
        else:
            instruction[KEY_VALUE] = ~get_value(instructions, instruction[KEY_OPERAND])
    else:
        operator_left = int(instruction[KEY_OPERAND_LEFT]) if instruction[KEY_OPERAND_LEFT].isdigit() else get_value(instructions, instruction[KEY_OPERAND_LEFT])
        operator_right = int(instruction[KEY_OPERAND_RIGHT]) if instruction[KEY_OPERAND_RIGHT].isdigit() else get_value(instructions, instruction[KEY_OPERAND_RIGHT])

        if instruction[KEY_OPERATOR] == GATE_AND:
            instruction[KEY_VALUE] = operator_left & operator_right
        elif instruction[KEY_OPERATOR] == GATE_OR:
            instruction[KEY_VALUE] = operator_left | operator_right
        elif instruction[KEY_OPERATOR] == GATE_LSHIFT:
            instruction[KEY_VALUE] = operator_left << operator_right
        elif instruction[KEY_OPERATOR] == GATE_RSHIFT:
            instruction[KEY_VALUE] = operator_left >> operator_right

    return instruction[KEY_VALUE]


def solve_part_i(inp: str, debug: bool = False):
    return get_value(initialize_instructions(inp), "a")


def solve_part_ii(inp: str, debug: bool = False):
    original_a_value = get_value(initialize_instructions(inp), "a")

    instructions = initialize_instructions(inp)
    instructions["b"] = {
        KEY_OPERATOR: ASSIGNMENT,
        KEY_VALUE: original_a_value
    }

    return get_value(instructions, "a")


solve(part=None, solver=solve_part_i, test_prefix=None, test_expected_results=None, debug=False)
solve(part=None, solver=solve_part_ii, test_prefix=None, test_expected_results=None, debug=False)
