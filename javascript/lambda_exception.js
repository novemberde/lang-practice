exports.handler = function(event, context, callback) {
    try{
        myHandler(event, context, callback)
    } catch (e) {
        callback(new Error("Internal Server Error"));
    }
}

const myHandler = (event, context, callback) => {
    throw new Error("hihi")
    
    callback(new Error("this is error"), {hi: "hi"});
}



exports.handler(null, null, function(err, result) {
    if(err) return console.error(err);
    
    console.log(result);
});