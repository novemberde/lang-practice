const test = () => {
    return new Promise((resolve, reject) => {
        // can be catched by promise when it occured an error;
        throw new Error("error asdfasd");
    });
}
const test2 = () => {
    return Promise.resolve()
    .then(() => {
        throw new Error("test2 error");
    });
}

test()
.then( result => {
    console.log(result);
})
.catch( err => {
    console.error(err);
});

test2()
.then( result => {
    console.log(result);
})
.catch( err => {
    console.error(err);
});