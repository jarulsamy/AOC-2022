def normalize_moves(parsed_input: list[(chr, chr)]) -> list[(chr, chr)]:
    move_map = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }
    return [(i[0], move_map[i[1]]) for i in parsed_input]


def score_pt1(move: (chr, chr)) -> int:
    their_move, my_move = move
    scores = {"A": 1, "B": 2, "C": 3}
    game_outcomes = {
        "A": {"A": 3, "B": 6, "C": 0},
        "B": {"A": 0, "B": 3, "C": 6},
        "C": {"A": 6, "B": 0, "C": 3},
    }
    my_score = scores[my_move]
    my_score += game_outcomes[their_move][my_move]
    return my_score


def score_pt2(move: (chr, chr)) -> int:
    their_move, outcome = move
    my_move_map = {
        "A": {"A": "C", "B": "A", "C": "B"},
        "B": {"A": "A", "B": "B", "C": "C"},
        "C": {"A": "B", "B": "C", "C": "A"},
    }
    my_move = my_move_map[their_move][outcome]
    return score_pt1((their_move, my_move))


def part_1(moves: list[(chr, chr)]):
    return sum(map(score_pt1, moves))


def part_2(moves: list[(chr, chr)]):
    return sum(map(score_pt2, moves))


if __name__ == "__main__":
    from pprint import pprint

    parsed_input = []
    with open("input", "r") as f:
        for i in f.readlines():
            i = i.strip()
            parts = i.split()
            parsed_input.append((parts[0], parts[1]))

    moves = normalize_moves(parsed_input)
    print(part_1(moves))
    print(part_2(moves))
