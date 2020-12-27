#[derive(Debug)]
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}
fn main() {
    let a = vec![1,2,3];
    println!("{:?}",a);

    let mut v = Vec::new();

    v.push(1);
    v.push(2);
    println!("{:?}", v);

    let b = vec![1,2,3,4,5];
    let third: &i32 = &b[2];
    let third: Option<&i32> = b.get(2);
    println!("{:?}", third);

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Float(0.12),
        SpreadsheetCell::Text(String::from("123")),
    ];
    println!("{:?}", row);
}