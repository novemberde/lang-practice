const {app, BrowserWindow}  = require("electron");

app.on('ready', () => {
  console.log("ready");
  console.log(app.getAppPath());
  console.log(app.getPath('home'));
  console.log(app.getPath('userData'));
  console.log(app.getPath('temp'));
  new BrowserWindow();
});

/**
will-finish-launching
ready
D:\Computer_related\lang-practice\javascript\Electron\codelab-1001
C:\Users\novem
C:\Users\novem\AppData\Roaming\codelab-1001
C:\Users\novem\AppData\Local\Temp
window-all-closed
before-quit
will-quit
quit
 */
app.on('window-all-closed', () => {
  console.log('window-all-closed');

  // default
  // app.quit();
  // 윈도우즈 환경일 경우 quit
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', (event) => {
  // event.preventDefault(); // 뒷단으로 못넘어가게 막는다.
  console.log("before-quit");
});

app.on('will-quit', (event) => {
  // event.preventDefault(); // 뒷단으로 못넘어가게 막는다.
  console.log("will-quit");
});

app.on('quit', () => {
  console.log("quit");
});

// mac전용 이벤트
app.on('activate', (event, hasVisibleWindows) => {
  // hasVisibleWindows : 창을 닫았을 때는 false
  console.log('activate', hasVisibleWindows);
});

app.on('will-finish-launching', () => {
  console.log('will-finish-launching');

});
