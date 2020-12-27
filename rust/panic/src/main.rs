use std::net::IpAddr;

pub struct Guess {
    value: u32,
}

impl Guess {
    pub fn new(value: u32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Geuss value must be between 1 and 100, got {}", value);
        }

        Guess {
            value
        }
    }

    pub fn value(&self) -> u32 {
        self.value
    }

    pub fn test(&self) -> u32 {
        self.value
    }

    pub fn test2() -> u32 {
        10
    }
}

fn main() {
    let home = "127.0.0.1".parse::<IpAddr>().unwrap();
    let home = "127.0.0.1".parse::<String>().unwrap();

    let g = Guess::new(10);
    let v = g.value();
    Guess::test2();
}
