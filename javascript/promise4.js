const test = () => {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, 1000, "Hello");
    });
}

test()
.then((result) => {
    return Promise.reject(new Error("hi"));
})
.catch(err => console.error(err));