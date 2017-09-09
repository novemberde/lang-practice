# TypeScript

- nvm
  - node version manager
```bash
$ nvm install 6.11.3
```
- n
  - like nvm, not support windows
  - github.com/tj/n
- nvs
  - node version switcher

```bash
$ npm install -g typescript
# 컴파일러 명령어
$ tsc <FilePath>
```

- Compiler
    - VS Code 에 컴파일러가 내장되어 있습니다.
    - 내장된 컴파일러 버전은 VS Code 가 업데이트 되면서 올라갑니다.
    - 그래서 컴파일러 버전과 VS Code 의 버전은 상관 관계가 있습니다.
    - 내장된 컴파일러를 선택할수 있고, 직접 설치한 컴파일러를 선택할 수도 있습니다.
  
- tslint
  - npm i typescript tslint (로컬)
  - tslint --init
  - tslint 플러그인 설치
```
$ ext install tslint
```
  - https://marketplace.visualstudio.com/items?itemName=eg2.tslint
  - https://palantir.github.io/tslint/


```bash
$ tsc --init
# 현재 폴더에 tsconfig.json파일이 있으면 설정정보에 따라 컴파일 실행
$ tsc
# watch 모드
$ tsc --watch
# 글로벌에서 지우고
$ npm uninstall typescript -g
# 현재 폴더에서만 사용
$ npm install typescript
$ node_modules/.bin/tsc
# package.json에 추가 "transpile": "node_modules/.bin/tsc" or "tsc"

# 8.4.0 부터 npx tsc 하면 된다. .bin에 있는 것을 사용할 수 있음
$ npx
```

