#[tokio::main]
async fn main() {
    /**
    Results:
        Hello, world!
        adding x: 1 and y: 2
        answer: 3
    */
    let t = try_it();
    println!("Hello, world!");
    t.await
}

async fn add(x: i32, y: i32) -> i32 {
    println!("adding x: {} and y: {}", x, y);
    x + y
}

async fn try_it() {
    let answer = add(1,2).await;
    println!("answer: {:?}", answer);
}

/****
fn add(x: i32, y: i32) -> i32 {
    println!("adding x: {} and y: {}", x, y);
    x + y
}

async fn try_it() {
    let answer = add(1,2);
    println!("answer: {:?}", answer);
}
*/