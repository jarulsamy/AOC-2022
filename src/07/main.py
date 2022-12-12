from pprint import pprint
from collections import defaultdict

# Let is represent the filesystem as a set of nested dicts
def ls(fs, cwd, lines_iter):
    cwd_obj = fs
    for i in cwd:
        cwd_obj = cwd_obj[i]

    line = None
    for i in lines_iter:
        if i.startswith("$"):
            line = i
            break
        tokens = i.split()
        if tokens[0] == "dir":
            cwd_obj[tokens[1]] = {}
        else:
            cwd_obj[tokens[1]] = int(tokens[0])

    return fs, cwd, lines_iter, line


def cd(cwd, dst):
    if dst == "/":
        cwd = ["/"]
    elif dst == "..":
        cwd = cwd[:-1]
    else:
        cwd.append(dst)
    return cwd


def dir_size(fs, path=None):
    size = 0
    cwd_obj = fs
    if path is not None:
        for i in path:
            cwd_obj = cwd_obj[i]

    for k, v in cwd_obj.items():
        if isinstance(v, dict):
            my_path = path[::]
            my_path.append(k)
            size += dir_size(fs, my_path)
        else:
            size += v

    return size


def get_dir_sizes(fs, path):
    sizes = {}

    cwd_obj = fs
    for i in path:
        cwd_obj = cwd_obj[i]

    key = "/".join(path[1:])
    sizes[f"/{key}"] = dir_size(fs, path)

    for k, v in cwd_obj.items():
        if not isinstance(v, int):
            my_path = path[::]
            my_path.append(k)
            sizes.update(get_dir_sizes(fs, my_path))

    return sizes


if __name__ == "__main__":
    with open("input", "r") as f:
        lines = [i.strip("\n") for i in f.readlines()]

    fs = {"/": {}}
    cwd = ["/"]

    lines_iter = iter(lines)
    line = next(lines_iter, None)
    while line:
        command, *args = line[1:].strip().split()
        if command == "ls":
            fs, cwd, lines_iter, line = ls(fs, cwd, lines_iter)
        elif command == "cd":
            cwd = cd(cwd, *args)
            line = next(lines_iter, None)
        else:
            raise ValueError(f"Unrecognized command: {command}")

    sizes = get_dir_sizes(fs, ["/"])

    # Part 1
    small_dir_sizes = [x for x in sizes.values() if x <= 100_000]
    print(sum(small_dir_sizes))

    # Part 2
    total_available_disk_space = 70_000_000
    target_available = 30_000_000

    total_used = dir_size(fs, ["/"])
    space_remaining = total_available_disk_space - total_used
    need_to_free = target_available - space_remaining

    candidates_for_deletion = [x for x in sizes.values() if x >= need_to_free]
    print(min(candidates_for_deletion))
