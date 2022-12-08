def part_1(parsed_input: list[int]) -> int:
    return max(parsed_input)


def part_2(parsed_input: list[int]) -> int:
    sorted_input = list(reversed(sorted(parsed_input)))
    return sum(sorted_input[:3])


if __name__ == "__main__":
    from pprint import pprint

    result: list[int] = []
    with open("input", "r") as f:
        current: list[int] = []
        for i in f.readlines():
            i = i.strip()
            if not i:
                result.append(sum(current))
                current = []
                continue
            current.append(int(i))

    print(part_1(result))
    print(part_2(result))
