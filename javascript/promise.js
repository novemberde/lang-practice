const test = () => {
    return new Promise((resolve, reject) => {
        // can be catched by promise when it occured an error;
        throw new Error("error asdfasd");
    });
}

test()
.then( result => {
    console.log(result);
})
.catch( err => {
    console.error(err);
});