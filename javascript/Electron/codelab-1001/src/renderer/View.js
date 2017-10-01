const { ipcRenderer, remote, shell } = require('electron');


class View {
  constructor () {
    this._btnSend = document.querySelector('#btn-send');
    this._btnSendSync = document.querySelector('#btn-send-sync');
    this._btnRemote = document.querySelector('#btn-remote');

    this._bindDomEvent();
    this._bindIpcEvent();
  }

  _bindIpcEvent () {
    ipcRenderer.on('bChannel', (event, arg) => {
      console.log(arg);
    });
  }

  _bindDomEvent () {
    this._btnSend.addEventListener('click', this._btnSendClick.bind(this));
    this._btnSendSync.addEventListener('click', this._btnSendSyncClick.bind(this));
    this._btnRemote.addEventListener('click', this._btnRemoteClick.bind(this));
  }

  _btnSendClick () {
    ipcRenderer.send('aChannel', {
      name: "HELLO"
    });
  }

  _btnSendSyncClick () {
    const result = ipcRenderer.sendSync('cChannel', {
      name: "HELLO-C"
    });

    console.log(result);
  }
  _btnRemoteClick () {
    console.log('remote');

    // main의 dialog를 쓸 수 있다.
    // 하지만 renderer 프로세스의 lifeCycle에 종속적이다.
    const { dialog, BrowserWindow } = remote;
    // dialog.showErrorBox("경고!!", "상세");
    // new BrowserWindow();
    // const win = remote.getCurrentWindow();
    // win.hide();

    // remote.getCurrentWebContents().openDevTools();
    // remote.getCurrentWindow().on(); // 이런식으로 쓰면 안됨!


    /**
     * shell 사용하기
     */ 
    // 대표 브라우저로 창 열기
    // shell.openExternal('https://github.com');
    // shell.openItem();

    /**
     * process 사용하기
     */
    
    console.log(process.versions);
    console.log(process.platform);
    console.log(process.type);

  }

}

module.exports = {
  View
};