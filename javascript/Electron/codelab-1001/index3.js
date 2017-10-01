const {app, BrowserWindow, Tray}  = require("electron");
const url = require('url')
const path = require('path');

const HTML = url.format({
  protocol: 'file',
  pathname: path.join(__dirname, 'index.html')
});
let win = null;

app.on('ready', () => {
  console.log('ready');
  
  // file protocol 없이 해도 됨.
  const tray = new Tray(path.join(__dirname, 'icon-16.png'));
  tray.on('click', () => {

    createWindow();
  });
  tray.on('right-click', () => {
    win.hide();
  });

  

});

app.on('window-all-closed', () => {

});

function createWindow () {
  if(win === null) {
    win = new BrowserWindow({
      show: false
    });

    win.on('closed', () => {
      win = null;
    });
  }

  return win.show();
}