fn main() {
    println!("Hello, world!");
    let mut s = String::new();

    let data = "initial contents";
    let s = data.to_string();
    let s = "initial contents".to_string();
    let s = String::from("initial contents");

    // UTF-8
    let hello = String::from("السلام عليكم");
    let hello = String::from("Dobrý den");
    let hello = String::from("Hello");
    let hello = String::from("שָׁלוֹם");
    let hello = String::from("नमस्ते");
    let hello = String::from("こんにちは");
    let hello = String::from("안녕하세요");
    let hello = String::from("你好");
    let hello = String::from("Olá");
    let hello = String::from("Здравствуйте");
    let hello = String::from("Hola");

    let s = "hello".to_string() + " world";
    let s = format!("hello {}", "world");
    let mut s = String::from("hello");
    s.push_str(" ");
    let s2 = "world";
    s.push_str(&s2);
    s.push('!');
    let s3 = s + &s2;

    let s = String::from("hello");
    let h = &s[0..4];
    let hello = "Здравствуйте";
    let s = &hello[0..4];

    // thread 'main' panicked at 'index 0 and/or 1 in `Здравствуйте` do not lie on character boundary'
    // let s = &hello[0..3];

    for c in "नमस्ते".chars() {
        println!("{}", c);
    }
    // न
    // म
    // स
    // ्
    // त
    // े

    for b in "नमस्ते".bytes() {
        println!("{}", b);
    }
    // 224
    // 164
    // 168
    // 224
}
