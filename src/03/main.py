import itertools
from functools import reduce


def grouper(iterable, n, fillvalue=None):
    """Group an interable into 'n' pieces.
    Fills the last piece with 'fillvalue' if necessary.

    Shamelessly stolen from itertools.
    """
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def get_priority(letter):
    if letter.islower():
        offset = ord("a")
    else:
        offset = ord("A") - 26

    return ord(letter) - offset + 1


def part_1(lines):
    total = 0
    for line in lines:
        half = len(line) // 2
        first_comp, second_comp = line[:half], line[half:]
        first_comp, second_comp = set(first_comp), set(second_comp)
        intersect = first_comp & second_comp
        total += sum(map(get_priority, intersect))

    return total


def part_2(lines):
    total = 0
    for group in grouper(iter(lines), 3):
        sets = [set(i) for i in group]
        badge_set = reduce(set.intersection, sets)
        total += sum(map(get_priority, badge_set))

    return total


if __name__ == "__main__":
    from pprint import pprint

    with open("input", "r") as f:
        lines = [i.strip() for i in f.readlines()]

    pprint(part_1(lines))
    pprint(part_2(lines))
