const {app, BrowserWindow, Tray, Menu, MenuItem, dialog}  = require("electron");
const url = require('url')
const path = require('path');
const fs = require('fs');

const HTML = url.format({
  protocol: 'file',
  pathname: path.join(__dirname, 'index.html')
});
let win = null;

app.on('ready', () => {
  console.log('ready');
  
  // file protocol 없이 해도 됨.
  const tray = new Tray(path.join(__dirname, 'icon-16.png'));
  tray.setContextMenu(getTrayMenu());
  // tray.on('click', () => {
  //   createWindow();
  // });
  // tray.on('right-click', () => {
  //   win.hide();
  // });
  createWindow();

  Menu.setApplicationMenu(getApplicationMenu());

});

app.on('window-all-closed', () => {

});

function createWindow () {
  if(win === null) {
    win = new BrowserWindow({
      show: false
    });
    win.loadURL(HTML);

    win.on('closed', () => {
      win = null;
    });
  }

  return win.show();
}

function getTrayMenu () {
  return Menu.buildFromTemplate([
    {
      type: 'normal', // defaultType
      label: "Open",
      click: createWindow
    },
    {
      type: 'separator'
    },
    {
      label: 'Quit',
      click: app.quit
    },
    {
      label: 'Lecture',
      submenu: [
        {
          label: "Electron"
        },
        {
          type: "checkbox",
          label: "CheckBox",
          checked: true,
          click: (e) => {
            this.checked = !e.checked;
          }
        }
      ]
    }
  ]);
}

function getApplicationMenu () {
  // default가 sub menu가 있어야함.
  return Menu.buildFromTemplate([
    {
      label: 'dialog',
      submenu: [
        {
          label: 'open',
          click: () => {
            dialog.showOpenDialog({}, (paths) => {
              if(paths !== undefined) {
                const buffer = fs.readFileSync(paths[0]);
                const object =  JSON.parse(buffer.toString());
                console.log(object.name);
              }
            });
          }
        },
        {
          label: 'save',
          click: () => {
            dialog.showSaveDialog({
              filters:[
                {
                  name: "this",
                  extension: "json"
                }
              ]
            }, (path) => {
              if(path !== undefined) {
                console.log(path);
                fs.writeFileSync(path, JSON.stringify({name: "hi"}));
              }
            });
            
          }
        },
        {
          label: 'message',
          click: () => {
            dialog.showMessageBox({
              message: "경고!",
              detail: "상세내용입니다.",
              buttons: [
                "확인",
                "취소"
              ],
              cancelId: 1// 취소버튼
            }, (id) => {
              console.log(id);
            });
          }
        },
      ]
    },
    {
      label: 'First',
      submenu: [
        {
          label: '1'
        },
        {
          label: '2'
        }
      ]
    },
    {
      label: 'Second',
      submenu: [
        {
          label: '1'
        },
        {
          label: '2'
        }
      ]
    },
    {
      label: 'Roles',
      submenu: [
        {
          role: 'paste'
        },
        {
          role: 'reload'
        },
        {
          role: 'about'
        },
        {
          role: 'toggledevtools'
        }
      ]
    }
  ]);
}