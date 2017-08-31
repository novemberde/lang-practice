const childe_process = require("child_process");

// console.log(process);

// process.exec("ls", (a, b) => {
//     console.log(a);
//     console.log(b);
// })

const exec = command => {
  return new Promise((resolve, reject) => {
    childe_process.exec(command, (err, stdout, stderr) => {
      if(err) return reject(stderr);
      return resolve(stdout);
    });
  });
}

exec("ls")
.then( result => console.log(result))
.catch( err => console.error(err));

exec("lsasdfad")
.then( result => console.log(result))
.catch( err => console.error(err));