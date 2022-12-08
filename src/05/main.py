import re
from copy import deepcopy
from itertools import tee


def parse_drawing(lines):
    drawing_lines = []
    rest = iter(lines)
    for i in rest:
        if i == "":
            break
        drawing_lines.append(i)

    stack_label = drawing_lines.pop()
    num_stacks = max(map(int, stack_label.split()))
    stacks = [[] for _ in range(num_stacks)]
    for line in drawing_lines:
        for i in range(num_stacks):
            crate = line[(i * 4) + 1]
            if crate != " ":
                stacks[i].insert(0, crate)

    return stacks, rest


def parse_action(action):
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    matches = pattern.match(action)
    n, src, dst = (int(i) for i in matches.groups())
    return n, src - 1, dst - 1


def crane_9000(action, stacks):
    n, src, dst = parse_action(action)

    # Stack => append to push
    #       => pop to take from top
    for i in range(n):
        item = stacks[src].pop()
        stacks[dst].append(item)

    return stacks


def crane_9001(action, stacks):
    n, src, dst = parse_action(action)
    src_size = len(stacks[src])
    items = stacks[src][src_size - n :]
    stacks[src] = stacks[src][:-n]
    stacks[dst] += items
    return stacks


def perform_actions(stacks, actions, func):
    for i in actions:
        stacks = func(i, stacks)

    tops = [i[-1] for i in stacks]
    print("".join(tops))


if __name__ == "__main__":
    with open("input", "r") as f:
        lines = [i.strip("\n") for i in f.readlines()]
    stacks, actions = parse_drawing(lines)
    a1, a2 = tee(actions)
    s1, s2 = deepcopy(stacks), deepcopy(stacks)

    perform_actions(s1, a1, crane_9000)
    perform_actions(s2, a2, crane_9001)
