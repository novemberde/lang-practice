let array = [];

for(let i=0; i<100; i++) array.push(i);

function* testGenerator() {
  yield array[1];
  yield array[2];
}

const tG = testGenerator();

console.log(tG.next()); //{ value: 1, done: false }
console.log(tG.next()); //{ value: 2, done: false }
console.log(tG.next()); //{ value: undefined, done: true }

