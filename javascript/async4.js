

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
        await f(i);    
    }
}

main();

Promise.resolve()
.then(() => {
    return main();
})
.catch(err => console.error(err));
/**
0
0
HELLO
(node:32906) UnhandledPromiseRejectionWarning: Unhandled promise rejection (rejection id: 1): HELLO
(node:32906) [DEP0018] DeprecationWarning: Unhandled promise rejections are deprecated. In the future, 
promise rejections that are not handled will terminate the Node.js process with a non-zero exit code.
 */