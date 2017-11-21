const bridge = {};
const myFunc = (num) => {
    if(bridge.gen.done) return;  
    setTimeout(() => {
        console.log(num);
        bridge.gen.next();
    }, 1000);
}

const myListener = (callback) => {
    callback();
}

function* myGen() {
    for(let i=0; i<10; i++) {
        yield myFunc(i);
    }
}

let gen = myGen();
bridge.gen = gen;
gen.next();
