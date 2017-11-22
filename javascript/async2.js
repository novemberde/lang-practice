function f(num) {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(num);
            resolve();
        }, 1000);
    });
}

async function main() {
    for(let i=0; i<10; i++) {

        await f(i);

    }
}

main();