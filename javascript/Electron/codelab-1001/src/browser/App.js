const { app, BrowserWindow, ipcMain } = require('electron');
const url = require('url')
const path = require('path');

const HTML = url.format({
  protocol: 'file',
  pathname: path.join(__dirname, '../../static/index.html')
});

class App {
  constructor () {
    this._win = null;
    app.on('ready', this._ready.bind(this));
  }

  _ready () {

    this._win = new BrowserWindow({
      show: false
    });

    this._win.once('ready-to-show', this._win.show);
    this._win.loadURL(HTML);

    // arg = { name: "HELLO" }
    ipcMain.on('aChannel', (event, arg) => {
      event.sender.send('bChannel', arg.name);
    });
    ipcMain.on('cChannel', (event, arg) => {
      event.returnValue = arg.name;
    });
    
  }
}

module.exports = {
  App
};