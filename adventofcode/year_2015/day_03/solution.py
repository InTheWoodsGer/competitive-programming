from adventofcode.utils import solve

MOVEMENTS = {
    "^": (1, 0),
    ">": (0, 1),
    "v": (-1, 0),
    "<": (0, -1)
}
MOVE_BY_SANTA, MOVE_BY_ROBO_SANTA = "santa", "robo-santa"


def solve_part_i(inp: str, debug: bool = False):
    current_position = (0, 0)
    visited_houses = {current_position}

    for direction in inp:
        movement = MOVEMENTS[direction]
        current_position = (current_position[0] + movement[0], current_position[1] + movement[1])
        visited_houses.add(current_position)

    if debug:
        print(f"  {visited_houses}")

    return len(visited_houses)


def solve_part_ii(inp: str, **kwargs):
    current_positions = {
        MOVE_BY_SANTA: (0, 0),
        MOVE_BY_ROBO_SANTA: (0, 0)
    }
    visited_houses = {(0, 0)}
    move_by = None

    for direction in inp:
        move_by = MOVE_BY_ROBO_SANTA if move_by == MOVE_BY_SANTA else MOVE_BY_SANTA
        movement = MOVEMENTS[direction]
        new_position = (current_positions[move_by][0] + movement[0], current_positions[move_by][1] + movement[1])

        current_positions[move_by] = new_position
        visited_houses.add(new_position)

    return len(visited_houses)


solve(part=None, solver=solve_part_i, test_prefix="test_01_", test_expected_results=[2, 4, 2])
solve(part=None, solver=solve_part_ii, test_prefix="test_02_", test_expected_results=[3, 3, 11])
