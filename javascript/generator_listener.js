const obj = {
    instance: null,
    length: 10,
    addOnNextListener: (o) => {
        this.instance = o.generator(obj.length);
    },
    generator: function* (length) {
        for(let i=0; i<length; i++) {
            yield obj.onNext(i);
        }
    },
    onNext: (num) => {
        // Worker Promise
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                console.log(num);
                resolve();
            }, 1000);
        });
    },
    next: () => {
        const result = this.instance.next();

        if(result.done) return;

        result.value
        .then(() => {
            return obj.next();
        })
        .catch(err => console.error(err));
    }
}

obj.addOnNextListener(obj);
obj.next();
