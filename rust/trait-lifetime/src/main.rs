use std::fmt::Display;

struct ImportantExcerpt<'a> {
    part: &'a str,
}

impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }

    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {}", announcement);
        self.part
    }
}

fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn longest_with_an_announcement<'a, T>(x: &'a str, y: &'a str, ann: T) -> &'a str
    where T: Display
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    // let r;
    // {
    //     let x = 5;
    //     r = &x;
    // }
    // println!("r: {}", r);
    //     error[E0597]: `x` does not live long enough
    //  --> src/main.rs:6:13
    //   |
    // 6 |         r = &x;
    //   |             ^^ borrowed value does not live long enough
    // 7 |     }
    //   |     - `x` dropped here while still borrowed
    // 8 |     println!("r: {}", r);
    //   |                       - borrow later used here

    let s = String::from("1");
    let result;

    {
        let s2 = String::from("xyz");
        result = longest(s.as_str(), s2.as_str());
        println!("{}", result);
    }

    let novel = String::from("Call me Ishmael, Some years ago...");
    let first_sentence = novel.split('.')
        .next()
        .expect("Could not find a '.'");
    let i = ImportantExcerpt { part: first_sentence };
}
