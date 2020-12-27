// This is not included in prelude different from String
// and doesn't have any macro.
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Red"), 50);

    let name = String::from("Red");
    scores.get(&name);

    for (k, v) in &scores {
        println!("{}: {}", k, v);
    }

    // Overwrite
    scores.insert(String::from("Red"), 20);
    for (k, v) in &scores {
        println!("{}: {}", k, v);
    }

    // insert if not exist
    scores.entry(String::from("Red")).or_insert(30);
    scores.entry(String::from("Black")).or_insert(30);
    for (k, v) in &scores {
        println!("{}: {}", k, v);
    }
}
