function f(num) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(num);
            reject("HELLO");
        }, 1000);
    });
}

async function main() {
    for(let i=0; i<10; i++) {
        try {
            await f(i);    
        } catch (error) {
            console.error(error);       
        }
    }
}

main();
/**
0
HELLO
1
HELLO
2
HELLO
3
HELLO
4
HELLO
5
HELLO
6
HELLO
7
HELLO
8
HELLO
9
HELLO

 */