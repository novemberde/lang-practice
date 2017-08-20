var iterations = 1000000;
console.time('Function #1');
var closureObj = function( a, b ) {
    var c = a + b;

    return {
        getA: function() {
            return a;
        },
        getB: function() {
            return b;
        },
        getC: function() {
            return c;
        },
        sayHello: function() {
            console.log("say");
        }
    };
}

var ConstructorObj = function(a, b) {
    this.a = a;
    this.b = b;
    this.c = a + b;

    this.sayHello = function() {
        console.log("say");
    }
}

for(var i = 0; i < iterations; i++ ){
    var a = closureObj("111111111111111111111111111111", "2222222222222222222222222222222");
    // console.log(a.getA());
};
console.timeEnd('Function #1')

console.time('Function #2');
for(var i = 0; i < iterations; i++ ){
    var a = new ConstructorObj("111111111111111111111111111111", "2222222222222222222222222222222");
    // console.log(a.a);
};
console.timeEnd('Function #2')