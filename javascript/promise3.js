const test = () => {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, 1000, "Hello");
    });
}

test()
.then((result) => {
    console.log(result);
})
.catch(err => console.error(err));