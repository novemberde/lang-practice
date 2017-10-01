[http://slides.com/woongjae/electron-basic](http://slides.com/woongjae/electron-basic)
[https://nwjs.io/](https://nwjs.io/)
[https://github.com/electron-userland](https://github.com/electron-userland)
[https://electronforge.io/](https://electronforge.io/)
[https://electron.atom.io/docs/api/menu-item/#roles](https://electron.atom.io/docs/api/menu-item/#roles)

Electron: 1.7.8	Node: 7.9.0	Chromium: 58.0.3029.110	V8: 5.8.283.38

1. Native Application
  - Javascript API를 통해 OS자원을 사용할 수 있기 때문에 Native라고도 한다.


Process가 Renderer process와 GPU process(default로 on되어 있음. canvas나 css에서 사용할 일이 있을 수도 있기 때문. 따로 설정해서 끌 수 있다)를 사용할 수 있음.

IPC(Inter process communication)를 통해 두 프로세스간 통신 가능.

- 브라우저 샌드박스가 아니다.
- 하지만 샌드박스로 만들수 있다.
- example: fs모듈을 사용할 수 있음. 보안을 신경 써봐야한다.

실행 환경(OS)에 따라 미리 정해진 폴더
// On macOS
electron/Electron.app/Contents/Resources/app/
├── package.json
├── main.js
└── index.html

// On Windows and Linux
electron/resources/app
├── package.json
├── main.js
└── index.html

npm install -g npx
npx electron . # npm 5.3버전 이상
