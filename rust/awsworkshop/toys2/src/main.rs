#[tokio::main]
async fn main() {
    // let answer = tokio::select! {
    //     fact_5 = fact_stiff(5) => fact_5,
    //     fact_10 = fact_stiff(10) => fact_10,
    // };
    // println!("answer: {}", answer);

    let answer = tokio::select! {
        fact_5 = fact_yielding(5) => fact_5,
        fact_10 = fact_yielding(10) => fact_10,
    };
    println!("answer: {}", answer);
}

async fn add(x: i32, y: i32) -> i32 {
    println!("adding x: {} and y: {}", x, y);
    x + y
}

async fn try_it() {
    let answer = add(1,2).await;
    println!("answer: {:?}", answer);
}

// Computes factorial of n, printing progress and yielding along the way.
async fn fact_yielding(n: u32) -> f64 {
    let mut i = 0_u32;
    let mut accum = 1_f64;
    loop {
        println!("i: {I} fact_{N}({I}): {A}", N=n, I=i, A=accum);
        if i == n {break;}
        tokio::task::yield_now().await;
        i += 1;
        accum *= i as f64;
    }
    return accum;
}

// Computes factorial of n, printing progress along the way.
async fn fact_stiff(n: u32) -> f64 {
    let mut i = 0_u32;
    let mut accum = 1_f64;
    loop {
        println!("i: {I} fact_{N}({I}): {A}", N=n, I=i, A=accum);
        if i == n { break; }
        i += 1;
        accum *= i as f64;
    }
    return accum;
}