const {app, BrowserWindow} = require("electron");
const url = require('url');
const path = require('path')

const html = url.format({
  protocol: "file",
  pathname: path.join(__dirname, 'index.html')
});

console.log(html);

app.on('ready', () => {
  const win = new BrowserWindow();
  win.loadURL(html);
});