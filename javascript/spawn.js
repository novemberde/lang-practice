const { spawn, spawnSync } = require('child_process');
// const ls = spawn('ls', ['-lh']);
const ls = spawnSync('ls', ['-lh']);
const ls2 = spawnSync('ls -al');
const awsS3 = spawnSync('aws', ['s3', 'ls']);

console.log(ls.output.toString());
console.log(ls2.error.toString());
console.log(awsS3.output.toString());

// ls.stdout.on('data', (data) => {
//   console.log(`stdout: ${data}`);
// });

// ls.stderr.on('data', (data) => {
//   console.log(`stderr: ${data}`);
// });

// ls.on('close', (code) => {
//   console.log(`child process exited with code ${code}`);
// });
