use std::fs;
use std::io;

fn read_input(input: &str) -> Result<Vec<u32>, io::Error> {
    let mut result: Vec<u32> = Vec::new();
    let mut current: u32 = 0;
    let file_contents: String = fs::read_to_string(input)?;
    for line in file_contents.lines() {
        if line == "" {
            result.push(current);
            current = 0;
        } else {
            current += line.parse::<u32>().unwrap();
        }
    }

    Ok(result)
}

fn part_1(input: &Vec<u32>) -> u32 {
    let mut max: u32 = 0;
    for i in input.iter() {
        if i > &max {
            max = *i;
        }
    }

    max
}

fn part_2(input: &mut Vec<u32>) -> u32 {
    let mut sum: u32 = 0;
    input.sort();
    for i in 0..input.len().min(3) {
        sum += input[input.len() - i - 1];
    }

    sum
}

fn main() {
    println!("Hello, world!");

    let mut input = read_input("input").expect("Unable to read input file");

    let part_1_result = part_1(&input);
    println!("{}", part_1_result);

    let part_2_result = part_2(&mut input);
    println!("{}", part_2_result);
}
