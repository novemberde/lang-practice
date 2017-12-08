
function f(num: Number) {
    return new Promise((resolve: any, reject:any): any => {
        setTimeout(() => {
            console.log(num);
            resolve();
        }, 1000);
    });
}

async function main() {
    for (let i = 0; i < 10; i++) {
        try {
            await f(i);
        } catch(error) {
            console.error(error);
        }
    }
}

main();