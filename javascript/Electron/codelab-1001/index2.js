const {app, BrowserWindow}  = require("electron");
const url = require('url')
const path = require('path');

const HTML = url.format({
  protocol: 'file',
  pathname: path.join(__dirname, 'index.html')
});

app.on('ready', () => {
  const second = new BrowserWindow({
    show: false,
    // frame: false, // 윈도우용
    // titleBarStyle: 'hidden'// 맥전용
    // titleBarStyle: 'hidden-inset'// 맥전용 상단바가 먹음
  });
  // const win = new BrowserWindow({
  //   x: 0,
  //   y: 0,
  //   width: 500,
  //   height: 500,
  //   // resizable: false,
  //   minWidth: 300,
  //   maxWidth: 700,
  //   minHeight: 500,
  //   maxHeight: 500,
  //   movable: true,
  //   show: false,
  //   maximizable: false,
  //   minimizable: false,
  //   closable: true,
  //   parent: second,
  //   modal: true
  // });
  

  // win.loadURL('https://github.com');
  // win.webContents.openDevTools();

  // // win.on('ready-to-show', () => {
  // //   win.show();
  // // });
  // // 처음 이벤트에만 반응하고 이벤트 리스너가 삭제된다.
  // win.once('ready-to-show', () => {
  //   win.show();
  // });
  second.once('ready-to-show', () => {
    second.show();
  });
  second.loadURL(HTML);
  second.on('focus', () => {
    console.log('focus');
  })
  second.on('blur', () => {
    console.log('blur');
  });
  second.on('move', () => {
    console.log('move');
  });


  console.log(BrowserWindow.getAllWindows());
  console.log(BrowserWindow.getFocusedWindow());
});