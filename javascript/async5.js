const f = (num) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(num);
        }, 1000);
    })
}

const main = async () => {
    for(let i=0; i<10; i++) {
        try {
            await f(i).then(n => console.log(n))
        } catch (error) {
            console.error(error);
        }
    }
}
