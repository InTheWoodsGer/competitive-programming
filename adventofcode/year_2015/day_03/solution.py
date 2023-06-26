from adventofcode.utils import solve


def solve_part_i(inp: str, debug: bool = False):
    position = (0, 0)
    visited_houses = {position}

    for direction in inp:
        if direction == "^":
            position = (position[0] + 1, position[1])
        elif direction == ">":
            position = (position[0], position[1] + 1)
        elif direction == "v":
            position = (position[0] - 1, position[1])
        elif direction == "<":
            position = (position[0], position[1] - 1)
        visited_houses.add(position)

    if debug:
        print(f"  {visited_houses}")

    return len(visited_houses)


def solve_part_ii(inp: str, **kwargs):
    progresses = [
        {"position": (0, 0), "visited_houses": {(0, 0)}},
        {"position": (0, 0), "visited_houses": {(0, 0)}}
    ]

    for i, direction in enumerate(inp):
        progress = progresses[i % 2]
        position = progress["position"]
        if direction == "^":
            progress["position"] = (position[0] + 1, position[1])
        elif direction == ">":
            progress["position"] = (position[0], position[1] + 1)
        elif direction == "v":
            progress["position"] = (position[0] - 1, position[1])
        elif direction == "<":
            progress["position"] = (position[0], position[1] - 1)
        progress["visited_houses"].add(progress["position"])

    return len(progresses[0]["visited_houses"].union(progresses[1]["visited_houses"]))


solve(part=None, solver=solve_part_i, test_prefix="test_01_", test_expected_results=[2, 4, 2], debug=True)
solve(part=None, solver=solve_part_ii, test_prefix="test_02_", test_expected_results=[3, 3, 11])
