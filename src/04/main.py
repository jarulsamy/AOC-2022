from dataclasses import dataclass


@dataclass
class IdRange:
    min: int
    max: int


def parse_range(r):
    minimum, maximum = r.split("-")
    return IdRange(int(minimum), int(maximum))


def fully_overlaps(first_r, second_r):
    first_r = parse_range(first_r)
    second_r = parse_range(second_r)

    if first_r.min > second_r.min:
        first_r, second_r = second_r, first_r
    elif first_r.min == second_r.min and first_r.max < second_r.max:
        first_r, second_r = second_r, first_r

    # First is now has the minimumn start (inclusive), if the max of first is
    # equal to or larger than the max of second, first fully encompasses
    # second.
    return first_r.max >= second_r.max


def overlaps(first_r, second_r):
    first_r = parse_range(first_r)
    second_r = parse_range(second_r)

    if first_r.min > second_r.min:
        first_r, second_r = second_r, first_r
    elif first_r.min == second_r.min and first_r.max < second_r.max:
        first_r, second_r = second_r, first_r

    # Second starts somewhere in first
    return second_r.min >= first_r.min and second_r.min <= first_r.max


def part_2(lines):
    overlap_count = 0
    for line in lines:
        first_elf, second_elf = line.split(",")
        if overlaps(first_elf, second_elf):
            overlap_count += 1

    return overlap_count


def count_if(func, lines):
    count = 0
    for line in lines:
        first_elf, second_elf = line.split(",")
        if func(first_elf, second_elf):
            count += 1

    return count


if __name__ == "__main__":
    with open("input", "r") as f:
        lines = [i.strip() for i in f.readlines()]

    print(count_if(fully_overlaps, lines))
    print(count_if(overlaps, lines))
