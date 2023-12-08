use std::fs;

fn main() {

    let file_path = "test.txt";
    let lines = fs::read_to_string(file_path).expect("Something went wrong reading the file");

    let split_lines: Vec<&str> = lines.split("\n").collect();
    println!("With text:\n{:?}", split_lines);
    let str_times: Vec<&str> = split_lines[0]
        .strip_prefix("Time:").unwrap()
        .trim()
        .split_whitespace().collect();
    let times: Vec<i32> = str_times.iter()
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let str_distances: Vec<&str> = split_lines[1]
        .strip_prefix("Distance:").unwrap()
        .trim()
        .split_whitespace().collect();
    let distances: Vec<i32> = str_distances.iter()
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    println!("Times: {:?}", times);
    println!("Distances: {:?}", distances);

    let mut winning_steps = ;
    for i in 0..times.len() {
        winning_steps.
        for offset in 1..times[i]{
            let remaining_time = times[i] - offset;
            let attempt_distance = remaining_time * offset;
            if attempt_distance > distances[i]{

            }

        }
    }


    
}


// def is_winning_way(race_duration, race_record, button_push_time):
    // remaining_time = race_duration - button_push_time
    // total_dist = remaining_time * button_push_time
    // if total_dist > race_record:
    //     return True
    // return False