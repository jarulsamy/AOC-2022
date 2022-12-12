def find_marker(line, n):
    for i in range(len(line)):
        my_set = line[i : i + n]
        if len(my_set) == len(set(my_set)):
            # All chars are unique
            return i + n

    return 0


if __name__ == "__main__":
    with open("input", "r") as f:
        line = f.read().strip()

    print(find_marker(line, 4))
    print(find_marker(line, 14))
