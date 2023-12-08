use std::fs;
use std::collections::HashMap;
use itertools::Itertools;  // itertools = "0.8"

#[derive(Debug, PartialEq, Eq, Hash, PartialOrd, Ord)]
enum HandType {
    FiveOfAKind = 7,
    FourOfAKind = 6,
    FullHouse = 5,
    ThreeOfAKind = 4,
    TwoPair = 3,
    OnePair = 2,
    HighCard = 1
}    


fn main() {
    fn compare_hand(hand_types: &HashMap<i32, HandType>, hands: &Vec<Vec<&str>>, a: &i32, b: &i32) -> std::cmp::Ordering {
        let card_score : HashMap<char, i32> = HashMap::from([
            ('A', 14),
            ('K', 13),
            ('Q', 12),
            // ('J', 11), - Part 1
            ('J', 1), //- Part 2
            ('T', 10),
            ('9', 9),
            ('8', 8),
            ('7', 7),
            ('6', 6),
            ('5', 5),
            ('4', 4),
            ('3', 3),
            ('2', 2)
        ]);
        let hand_a = &hand_types.get(&a);
        let hand_b = &hand_types.get(&b);
        let mut c = hand_a.cmp(hand_b);
        if c.is_eq(){
            let mut i = 0;
            while c.is_eq(){
                let char_a = hands[*a as usize][0].chars().nth(i).unwrap();
                let char_b = hands[*b as usize][0].chars().nth(i).unwrap();
                c = card_score.get(&char_a).cmp(&card_score.get(&char_b));
                i += 1;
            }
        }
        return c
    }



    let file_path = "input.txt";
    let lines = fs::read_to_string(file_path).expect("Something went wrong reading the file");
    let split_lines: Vec<&str> = lines.split("\n").collect();
    let hands: Vec<Vec<&str>>  = split_lines.iter()
    .map(|s| s.split(' ').collect())
    .collect();


    let mut hand_types: HashMap<i32, HandType> = HashMap::new();

    for i in 0..hands.len(){
        let hand = &hands[i];
        let cards = hand[0];
        let bid = hand[1].parse::<i32>().unwrap();
        let char_vec: Vec<char> = cards.chars().collect();

        let mut letter_counts: HashMap<char,i32> = HashMap::new();
        for c in char_vec {
            *letter_counts.entry(c).or_insert(0) += 1;
        }

        let j_count = letter_counts.get(&'J').unwrap_or(&0);
        println!("{:?}", j_count);

        let mut hand_type: HandType = HandType::HighCard;
        if letter_counts.len() == 1{
            // Five of a kind
            hand_type = HandType::FiveOfAKind;
        } else if letter_counts.len() == 2{
            let values: Vec<&i32> = letter_counts.values().collect();

            if j_count > &0  {
                hand_type = HandType::FiveOfAKind
            } else if values.contains(&&4){
                // Four of a kind
                hand_type = HandType::FourOfAKind;
            } else {
                // Full house
                hand_type = HandType::FullHouse;
            }
        } else if letter_counts.len() == 3{
            let values: Vec<&i32> = letter_counts.values().collect();
            println!("{:?} - {:?}", hand,values);
            if values.contains(&&3){
                if j_count > &0 {
                    hand_type= HandType::FourOfAKind
                }else{
                    // Three of a kind
                    hand_type = HandType::ThreeOfAKind;
                }
            } else {
                if j_count == &1 {
                    hand_type= HandType:: FullHouse
                } else  if j_count == &2 {
                    hand_type= HandType:: FourOfAKind
                }else{
                    // Two pair
                    hand_type = HandType::TwoPair;
                }
            }
        } else if letter_counts.len() == 4{
            if j_count > &0 {
                hand_type= HandType::ThreeOfAKind
            } else {
            // One pair
            hand_type = HandType::OnePair;
            }
        } else if letter_counts.len() == 5{
            if j_count > &0 {
                hand_type= HandType::OnePair
            } else {
                // High card
                hand_type = HandType::HighCard;
            }
        } else {
            panic!("Error: hand has {} cards", letter_counts.len());
        }

        hand_types.insert(i as i32, hand_type);
    }
    println!("{:?}", hand_types);
    let sorted_index:Vec<&i32> = hand_types.keys()
    .sorted_by(|a,b| compare_hand(&hand_types, &hands, a, b))
    .collect();
    println!("{:?}", sorted_index);
    let mut total = 0;
    for i in 0..sorted_index.len(){
        let card_index = sorted_index[i];
        total += hands[*card_index as usize][1].parse::<i32>().unwrap() * (i as i32 + 1);
        println!("{} - {:?} - {} * {}", hands[*card_index as usize][0], hand_types[&card_index], hands[*card_index as usize][1].parse::<i32>().unwrap(), i as i32 + 1);
    }
    println!("{}", total)

}

