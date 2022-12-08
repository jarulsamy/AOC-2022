use std::fs;
use std::io;

fn score(their_move: char, my_move: char) -> u8 {
    let my_move_decoded = (my_move as u8 - 23) as char;

    let game_outcome = match their_move {
        'A' => match my_move_decoded {
            'A' => 3,
            'B' => 6,
            'C' => 0,
            _ => 0,
        },
        'B' => match my_move_decoded {
            'A' => 0,
            'B' => 3,
            'C' => 6,
            _ => 0,
        },
        'C' => match my_move_decoded {
            'A' => 6,
            'B' => 0,
            'C' => 3,
            _ => 0,
        },
        _ => 0,
    };

    let shape_score = my_move_decoded as u8 - 64;
    game_outcome + shape_score
}

fn score_pt2(their_move: char, my_move: char) -> u8 {
    let mut my_move_score: u8;
    let shape_score = my_move_decoded as u8 - 64;
    game_outcome + shape_score
}

fn read_input(filename: &str) -> Result<Vec<(char, char)>, io::Error> {
    let file_contents = fs::read_to_string(filename)?;
    let mut result: Vec<(char, char)> = Vec::new();
    for i in file_contents.lines() {
        result.push((i.chars().nth(0).unwrap(), i.chars().nth(2).unwrap()));
    }

    Ok(result)
}

fn part_1(input: &Vec<(char, char)>) -> u32 {
    let sum: u32 = input
        .iter()
        .fold(0, |acc, game| acc + score(game.0, game.1) as u32);
    sum
}

fn part_1(input: &Vec<(char, char)>) -> u32 {
    let sum: u32 = input
        .iter()
        .fold(0, |acc, game| acc + score_pt2(game.0, game.1) as u32);
    sum
}

fn main() {
    println!("Hello, world! 2");

    let input = read_input("input").expect("Could not read input file");
    let part1_result = part_1(&input);
    println!("{}", part1_result);
    // println!("{}", score('A', 'Y'));
}
