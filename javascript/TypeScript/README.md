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

VSCode의 problems를 통해 힌트를 볼 수 있다.

- Compiler
    - VS Code 에 컴파일러가 내장되어 있습니다.
      - 실제로 컴파일을 해주진 않는다. 따로 컴파일러 돌려야 함.
    - 내장된 컴파일러 버전은 VS Code 가 업데이트 되면서 올라갑니다.
    - 그래서 컴파일러 버전과 VS Code 의 버전은 상관 관계가 있습니다.
    - 내장된 컴파일러를 선택할수 있고, 직접 설치한 컴파일러를 선택할 수도 있습니다.
  
- tslint
  - npm i typescript tslint (로컬)
  - npm i tslint -D
  - tslint --init
  - tslint 플러그인 설치
```
$ ext install tslint
```
  - https://marketplace.visualstudio.com/items?itemName=eg2.tslint
  - https://palantir.github.io/tslint/

node_modules/.bin/tslint --init


## Compiler option

최상위 프로퍼티
- compileOnSave
  - watch로 해결, atom 에디터에서는 필요할지도?
- extends
  - 해당파일의 설정을 상속받는다.
- compileOptions
- files
- include
- exclude
- typeAcquisition

typescript 1.0과 2.0의 차이
- 이미 만들어져 있는 모듈들을 사용하기 어려웠음
- 타입스크립트에서 자바스크립트를 가져오면 타입을 알아볼 수 없이 나와버리니 사용하기 어려움
- type이 항상 any로 나왔기 때문에
- 그렇기 때문에 javascript에 대응하는 파일이 필요했음 => 관리의 어려움
- typings 등등 npm모듈로 사용하는 방식... 이미 사라져감.

타입만 넣어서 설치할 때 
npm i -D @types/superagent

```json
{
  compilerOptions: {
    target: "es5"
    module: "commonjs"
    typeRoots: [
      "",
      ""
    ]
  }
}
```

@types
TypeScript 2.0 부터 사용 가능해진 내장 type definition 시스템
아무 설정을 안하면 ?
  node_modules/@types 라는 모든 경로를 찾아서 사용
typeRoots 를 사용하면 ?
  배열 안에 들어있는 경로들 아래서만 가져옵니다.
types 를 사용하면 ?
  배열 안의 모듈 혹은 ./node_modules/@types/ 안의 모듈 이름에서 찾아옵니다.
  [] 빈 배열을 넣는다는건 이 시스템을 이용하지 않겠다는 것입니다.
typeRoots 와 types 를 같이 사용하지 않습니다.


target 과 lib
target
  빌드의 결과물을 어떤 버전으로 할 것이냐
  지정을 안하면 es3 입니다.
lib
  기본 type definition 라이브러리를 어떤 것을 사용할 것이냐
lib 를 지정하지 않을 때,
  target 이 'es3' 이고, 디폴트로 lib.d.ts 를 사용합니다.
  target 이 'es5' 이면, 디폴트로 dom, es5, scripthost 를 사용합니다.
  target 이 'es6' 이면, 디폴트로 dom, es6, dom.iterable, scripthost 를 사용합니다.
​lib 를 지정하면 그 lib 배열로만 라이브러리를 사용하니다.
​빈 [] => 'no definition found 어쩌구'

```json
compileOptions : target 과 lib
{
    "type": "object",
    "description": "Instructs the TypeScript compiler how to compile .ts files.",
    "properties": {
        "target": {
            "description": "Specify ECMAScript target version. Permitted values are 'es3', 'es5', 'es2015', 'es2016', 'es2017' or 'esnext'.",
            "type": "string",
            "default": "es3", //polyfill 로 es3로 변환해야함. default라고 써 있지만 문제있음
            "anyOf": [  // 내가 작성한 문법이 enum인 것은 바꾸지 말아라.
                {
                    "enum": [
                        "es3",
                        "es5",
                        "es2015",
                        "es2016",
                        "es2017",
                        "esnext"
                      ]
                }, {
                      "pattern": "^([eE][sS]([356]|(201[567])|[nN][eE][xX][tT]))$"
                }
            ]
        },
        "lib": {  // 코어 자바스크립트 엔진에 대한 타입이 되어 있음. const a = 1; a.<HINT>; document.getElement~~~ ... etc// lib.d.ts // lib.es6.d.ts
            "description": "Specify library file to be included in the compilation. Requires TypeScript version 2.0 or later.",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [ "es5", "es6", "es2015", "es7", "es2016", "es2017", "esnext", "dom", "dom.iterable", "webworker", "scripthost", "es2015.core", "es2015.collection", "es2015.generator", "es2015.iterable", "es2015.promise", "es2015.proxy", "es2015.reflect", "es2015.symbol", "es2015.symbol.wellknown", "es2016.array.include", "es2017.object", "es2017.sharedmemory", "esnext.asynciterable"
                ]
            }
        },
        "noLib": {
            "description": "Do not include the default library file (lib.d.ts).",
            "type": "boolean"
        }
    }
}
```




compileOptions : outDir, outFile 

compileOptions : module


backpack - backend webpack

command shift b // 명령창 볼 수 있음

src / output
src / gist


여러 선택할 수 있는 모듈 스타일
AMD / UMD / commonjs 

```json
{
    "type": "object",
    "description": "Instructs the TypeScript compiler how to compile .ts files.",
    "properties": {
        "module": {
            "description": "Specify module code generation: 'none', 'CommonJS', 'Amd', 'System', 'UMD', or 'es2015'.",
            "enum": [ "commonjs", "amd", "umd", "system", "es6", "es2015", "none" ]
        },
        "moduleResolution": {
            "description": "Specifies module resolution strategy: 'node' (Node) or 'classic' (TypeScript pre 1.6) .",
            "type": "string",
            "pattern": "^(([Nn]ode)|([Cc]lassic))$",
            "default": "classic"
        },
        "baseUrl": {
            "description": "Base directory to resolve non-relative module names.",
            "type": "string"
        },
        "paths": {
            "description": "Specify path mapping to be computed relative to baseUrl option.",
            "type": "object"
        },
        "rootDirs": {
            "description": "Specify list of root directories to be used when resolving modules.",
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    }
}
```
- module
  - 컴파일 된 모듈의 결과물을 어떤 모듈 시스템으로 할지를 결정
  - target 이 'es6' 이면 es6 가 디폴트이고,
  - target 이 'es6' 가 아니면 commonjs 가 디폴트 입니다.
  - AMD 나 System 와 사용하려면, outFile 이 지정되어야 합니다.
  - ES6 나 ES2015 를 사용하려면, target 이 es5 이하여야 합니다.
- moduleResolution
  - ts 소스에서 모듈을 사용하는 방식을 지정해야 합니다.
  - Classic 아니면 Node 입니다.
  - CommonJS 일때만 Node 라고 생각하시면 됩니다.
- paths 와 baseUrl
  - 상대경로 방식이 아닌 baseUrl 로 꼭지점과 paths 안의 키/밸류로 모듈을 가져가는 방식입니다.
  - rootDirs : 배열 안에서 상대 경로를 찾는 방식입니다.


React app TypeScript 기반으로 생성
- create-react-app app-name --scripts-version=react-scripts-ts
- [react-&-webpack in typescript](https://www.typescriptlang.org/docs/handbook/react-&-webpack.html)

awesome typescript loader 또는 ts-loader를 사용.(기존에는 Babel 사용)
- 프로젝트 만들어서 tsconfig.json 확인


```bash
# 현재 폴더를 기준으로 편집기 열기
$ code .
```

## TypeScript Basic Types

- TypeScript 에서 프로그램 작성을 위해 기본 제공하는 데이터 타입
- 사용자가 만든 타입은 결국은 이 기본 자료형들로 쪼개집니다.
- JavaScript 기본 자료형을 포함 (superset)
  - ECMAScript 표준에 따른 기본 자료형은 6가지
    - Boolean
    - Number
    - String
    - Null
    - Undefined
    - Symbol (ECMAScript 6 에 추가)
    - Array : object 형
- 프로그래밍을 도울 몇가지 타입이 더 제공된다.
  - Any
  - Void
  - Never
  - Enum
  - Tuple : object 형


#### Primitive Type
오브젝트와 레퍼런스 형태가 아닌 실제 값을 저장하는 자료형

프리미티브 형의 내장 함수를 사용 가능한 것은 자바스크립트 처리 방식 덕분

FlyWeight pattern. 숫자를 스트링으로 변환하는 경우. 순간적으로 object로 변환하여 값을 리턴

#### Literal
값 자체가 변하지 않는 값을 의미.
```js
35; // number 리터럴
"mark"; // string 리터럴
true; // boolean 리터럴

{
  name: "mark",
  age: 35
}
```
"리터럴  상수는 5, 1.23   과  같은  숫자나, 과 같은 문자열 등을 말합니다. 'This  is  a  string'   혹은 "It’s  a  string!"이것들이  리터럴  상수라고  불리우는  이유는  이것들이  프로그램  내에  직접  문자  형태로(literally)지정되는  값들이기  때문입니다.  이러한  값들은  한번  지정되면  변하지  않습니다.  예를  들면  숫자2   는  언제나  자기  자신이  2라는  숫자임을  나타내며  어떤  다른  의미도  갖지  않습니다.  이들은  한번  지정되면  그  값을  변경할  수  없기  때문에  _상수_입니다.  그  중에서도  특별히  이러한  값들을  리터럴 상수라고 부릅니다." 

#### Boolean / boolean 두개가 다름.
- 가장 기본적인 데이터 타입
- 단순한 true 혹은 false 값 입니다.
- JavaScript / TypeScript 에서 'boolean' 이라고 부른다.

```js
 let isDone: boolean = false;

typeof isDone === 'boolean' // true

// Type 'boolean' is assignable to type 'Boolean'.
let isOk: Boolean = true;

// Type 'Boolean' is not assignable to type 'boolean'.
// 'boolean' is a primitive, but 'Boolean' is a wrapper object.
// Prefer using 'boolean' when possible.
let isNotOk: boolean = new Boolean(true);
```

#### Number
- JavaScript 와 같이, TypeScript 의 모든 숫자는 부동 소수점 값 입니다.
- TypeScript는 16진수 및 10진수 리터럴 외에도, ECMAScript 2015에 도입된 2진수 및 8진수를 지원합니다.
```js
let decimal: number = 6; // 10진수 리터럴
let hex: number = 0xf00d; // 16진수 리터럴
let binary: number = 0b1010; // 2진수 리터럴
let octal: number = 0o744; // 8진수 리터럴
```
#### Template String
- 행에 걸쳐 있거나, 표현식을 넣을 수 있는 문자열
- 이 문자열은 backtick (= backquote) 기호에 둘러쌓여 있습니다.
- 포함된 표현식은 `${ expr }` 와 같은 형태로 사용합니다.

```js
let fullName: string = `Bob Bobbington`;
let age: number = 37;

let sentence: string = `Hello, my name is ${ fullName }.

I'll be ${ age + 1 } years old next month.`;

// template string 을 사용하지 않을 경우
let sentence: string = "Hello, my name is " + fullName + ".\n\n" +
    "I'll be " + (age + 1) + " years old next month.";
```
#### Undefined & Null
TypeScript 에서 'undefined' 와 'null' 은 실제로 각각 'undefined' 와 'null' 이라는 고유한 타입을가집니다.
'void' 와 마찬가지로, undefined 와 null 은 그 자체로는 쓸모가 없습니다.
둘다 소문자만 존재합니다.
 // 이 변수들에 할당할 수 있는 것들은 거의 없다.
```js
let u: undefined = undefined;
let n: null = null;
```

- undefined & null are subtypes of all other types.
  - 기본 설정이 그렇습니다.
  - number 에 null 또는 undefined 를 할당할 수 있다는 의미입니다.
  - 하지만, 컴파일 옵션에서 `--strictNullChecks`사용하면, null 과 undefined 는 void 나 자기 자신들에게만 할당할 수 있습니다.
  - 이 경우, null 과 undefined 를 할당할 수 있게 하려면, union type 을 이용해야 합니다.
```js
let name: string = null;
let age: number = undefined;

// strictNullChecks => true
// Type 'null' is not assignable to type 'string'.
let name: string = null; (X)

// null => null || void, undefined => undefined || void
// Type 'null' is not assignable to type 'undefined'.
let u: undefined = null; // (X)

let v: void = undefined; // (O)

let union: string | null | undefined = 'str';
```

- null in JavaScript 
  - null 이라는 값으로 할당된 것을 null 이라고 합니다.
  - 무언가가 있는데, 사용할 준비가 덜 된 상태.
  - null 이라는 타입은 null 이라는 값만 가질 수 있습니다.
  - 런타임에서 typeof 연산자를 이용해서 알아내면, object 입니다.
```js
let n: null = null;

console.log(n); // null
console.log(typeof n); // object // Runtime에서 type이 계산됨.
```

- undefined in JavaScript 
  - 값을 할당하지 않은 변수는 undefined 라는 값을 가집니다.
  - 무언가가 아예 준비가 안된 상태
  - object 의 property 가 없을 때도 undefined 입니다.
  - 런타임에서 typeof 연산자를 이용해서 알아내면, undefined 입니다.
```js
let u: undefined = undefined;

console.log(u); // undefined
console.log(typeof u); // undefined // Runtime에서 type이 계산됨.
```

#### Void
- 타입이 없는 상태입니다.
- `any` 와 반대의 의미를 가집니다.
- Void 는 없습니다. 소문자입니다.
- 주로 함수의 리턴이 없을 때 사용합니다. 그 외에는 사용할 일이 거의 없습니다.
```js
function returnVoid(message): void {
  console.log(message);
}

returnVoid('리턴이 없다');
```

#### Any
- 어떤 타입이어도 상관없는 타입입니다.
- 이걸 최대한 쓰지 않는게 핵심입니다.
- 왜냐면 컴파일 타임에 타입 체크가 정상적으로 이뤄지지 않기 때문입니다.
- 그래서 컴파일 옵션 중에는 any 를 쓰면 오류를 뱉도록 하는 옵션도 있습니다.

#### noImplicitAny
```js
function returnAny(message): any {
  console.log(message);
}

returnVoid('리턴은 아무거나');
```

#### Never
리턴에 주로 사용됩니다.
아래 3가지 정도의 경우가 대부분입니다.
```js
// Function returning never must have unreachable end point
function error(message: string): never {
    throw new Error(message);
}

// Inferred return type is never
function fail() {
    return error("Something failed");
}

// Function returning never must have unreachable end point
function infiniteLoop(): never {
    while (true) {
    }
}
```

#### Array
- 원래 자바스크립트에서 array 는 객체입니다.
- 사용방법
  - Array<타입>
  - 타입[]

```js
let list: number[] = [1, 2, 3];

let list: Array<number> = [1, 2, 3];
```

#### Tuple
- 배열인데 타입이 한가지가 아닌 경우
- 마찬가지로 객체입니다.
- 꺼내 사용할때 주의가 필요합니다.
- 배열을 Destructuting 하면 타입이 제대로 얻어집니다.
```js
// Declare a tuple type
let x: [string, number];
// Initialize it
x = ["hello", 10]; // OK
// Initialize it incorrectly
x = [10, "hello"]; // Error

x[3] = "world"; // OK, 'string' can be assigned to 'string | number'

console.log(x[5].toString()); // OK, 'string' and 'number' both have 'toString'

x[6] = true; // Error, 'boolean' isn't 'string | number'

const person: [string, number] = ['mark', 35, "a", 4];

const [name, age] = person;
```

#### Enum
- C 에서 보던것과 같습니다.
- 아래 예제만 이해하면 사용 준비 끝
```js
enum Color {Red, Green, Blue}
let c: Color = Color.Green;

enum Color {Red = 1, Green, Blue}
let c: Color = Color.Green;

enum Color {Red = 1, Green = 2, Blue = 4}
let c: Color = Color.Green;

enum Color {Red = 1, Green, Blue}
let colorName: string = Color[2];
```

#### Symbol
- ECMAScript 2015 의 Symbol 입니다.
- 프리미티브 타입의 값을 담아서 사용합니다.
- 고유하고 수정불가능한 값으로 만들어줍니다.
- 그래서 주로 접근을 제어하는데 쓰는 경우가 많았습니다.
```js
let sym = Symbol();

let obj = {
    [sym]: "value"
};

console.log(obj[sym]); // "value"
```

#### var VS let, const
- var
    - ES5
    - 변수의 유효 범위 : 함수 스코프
    - 호이스팅 (O)
    - 재선언 가능
- let, const
    - ES6
    - 변수의 유효 범위 : 블록 스코프 (친숙)
    - 호이스팅 (X)
    - 재선언 불가
    - var 말고 let, const
```js
console.log(hoisted_var);

var hoisted_var = '변수를 아래서 선언했는데 사용이 위에서 가능';

////////////////////////////////////////

console.log(hoisted_let);

let hoisted_let = '변수를 아래서 선언했는데 사용이 위에서 불가';
```

redeclare
```js
var redeclare_var: string = '한번 선언 했는데';
var redeclare_var: string = '또 선언이 가능';
// var redeclare_var: number = 0; (X)

////////////////////////////////////////

let redeclare_let = '한번 선언 했기 때문에';
let redeclare_let = '또 선언이 불가';
/*
그렇지만 var 에서 재선언 하더라도 같은 타입이어야 함.
*/
```

let 과 const 의 타입 추론
```js
let a: string = '에이';
let b = '비이';

const c: string = '씨이';
const d = '디이';
const dd = {
  aaa: "aa"
};
dd.aaa = "123"; // string으로 가능.
dd.aaa = 123; // error
dd.bbb = '';  // error 
/*
1. a 는 명시적으로 지정된 타입인 string
2. b 는 타입추론에 의한 타입인 string
3. c 는 명시적으로 지정된 타입인 string
4. d 는 타입추론에 의한 타입인 리터럴타입 "디이"
5. dd 는 {ddd:string}으로 나옴
*/
```

## Type assertion
- 적당한 번역을 찾을 수가 없었습니다.
  - Type assertions
- 형변환과는 다릅니다.
  - 형변환은 실제 데이터 구조를 바꿔줍니다.
- '타입이 이것이다' 라고 컴파일러에게 알려주는 것을 의미합니다.
  - 그래서 행동에 대해서 작성자가 100% 신뢰하는 것이 중요합니다.
- 문법적으로는 두가지 방법이 있습니다.
  - 변수 as 강제할타입
  - <강제할타입>변수

sample code
```typescript
let someValue: any = "this is a string";

let strLength: number = (<string>someValue).length;
let strLength: number = (someValue as string).length;

// Input Element로 강제하기
const a = document.getElementById('test') as HTMLInputElement; 
a.value;

/*
1. 주로 넓은 타입에서 좁은 타입으로 강제하는 경우가 많다.
2. jsx 에서는 as 를 쓴다.
*/
```

## Type Alias

- 타입 별칭 (별명)
  - 인터페이스랑 비슷해 보입니다.
  - Primitive, Union Type, Tuple
  - 기타 직접 작성해야하는 타입을 다른 이름을 지정할 수 있습니다.
  - 만들어진 타입의 refer 로 사용하는 것이지 타입을 만드는것은 아닙니다.

#### Aliasing Primitive
```typescript
type MyStringType = string;

const str = 'world';

let myStr: MyStringType = 'hello';
myStr = str;

/*
별 의미가 없다..
*/
```

#### Aliasing Union Type
```typescript
let person: string | number = 0;
person = 'Mark';

type StringOrNumber = string | number;

let another: StringOrNumber = 0;
another = 'Anna';

/*
1. 유니온 타입은 A 도 가능하고 B 도 가능한 타입
2. 길게 쓰는걸 짧게
*/
```

#### Aliasing Tuple
```typescript
let person: [string, number] = ['Mark', 35];

type PersonTuple = [string, number];

let another: PersonTuple = ['Anna', 24];

/*
1. 튜플 타입에 별칭을 줘서 여러군데서 사용할 수 있게 한다.
*/
```

#### Interface 와의 차이점 (1)
```typescript
type Alias = { num: number }

interface Interface {
    num: number;
}

declare function aliased(arg: Alias): Alias;
declare function interfaced(arg: Interface): Interface;

/*

1. type alias 는 object literal type 로
2. interface 는 interface 로

*/
```

#### Interface 와의 차이점 (2)
```typescript
type PersonAlias = {
    name: string;
    age: number;
};

interface IPerson extends PersonAlias {

}

let ip: IPerson = {
    name: 'Mark',
    age: 35
};

class PersonImpl implements PersonAlias {
    name: string;
    age: number;

    hello() {
        console.log('안녕하세요');
    }
}

let pi: PersonImpl = new PersonImpl();
pi.hello();

class PersonChild extends PersonAlias {
}

/*

1. 당연한건 type alias 끼리는 extends, implements 불가
2. interface extends type alias 가능
3. class implements type alias 가능
4. class extends type alias 블가 (interface 도 마찬가지)
5. 마치 interface 처럼 동작한다.

*/
```

## Interface

#### interface - basic
```typescript
function hello(person: { name: string; age: number; }): void {
    console.log(`안녕하세요! ${person.name} 입니다.`);
}

const p: { name: string; age: number; } = {
    name: 'Mark',
    age: 35
};

hello(p); // 안녕하세요! Mark 입니다.

///////////////////////////////////////////////////////////////

function hello(person: { name: string; age: number;}): void {
    console.log(`안녕하세요! ${person.name} 입니다.`);
}

const p: Person = {
    name: 'Mark',
    age: 35
};

hello(p);

///////////////////////////////////////////////////////////////

interface Person {
    name: string;
    age: number;
}

function hello(person: Person): void {
    console.log(`안녕하세요! ${person.name} 입니다.`);
}

const p: Person = {
    name: 'Mark',
    age: 35
};

hello(p); // 안녕하세요! Mark 입니다
```


#### interface - optional property (1)
```typescript
interface Person {
    name: string;
    age?: number; // 있거나 없거나!
}

function hello(person: Person): void {
    console.log(`안녕하세요! ${person.name} 입니다.`);
}

const p1: Person = {
    name: 'Mark',
    age: 35
};

const p2: Person = {
    name: 'Anna'
};

hello(p1); // 안녕하세요! Mark 입니다.
hello(p2); // 안녕하세요! Anna 입니다.
```

#### interface - optional property (2)

Indexable Type

```typescript
interface Person {
    name: string;
    age?: number;
    // number 또는 string만 지정 가능하다. props대신 index라고 쓰기도함
    [props: string]: any;
}

function hello(person: Person): void {
    console.log(`안녕하세요! ${person.name} 입니다.`);
}

const p1: Person = {
    name: 'Mark',
    age: 35,
};

const p2: Person = {
    name: 'Anna',
    systers: [
        'Sung',
        'Chan'
    ]
};

const p3: Person = {
    name: 'Bokdaengi',
    father: p1,
    mother: p2
};
```


#### interface - function in interface
```typescript
interface Person {
    name: string;
    age: number;
    hello(): void;
}

const p1: Person = {
    name: 'Mark',
    age: 35,
    hello: function (): void {
        console.log(this);
        console.log(`안녕하세요! ${this.name} 입니다.`);
    }
};

const p2: Person = {
    name: 'Mark',
    age: 35,
    hello(): void {
        console.log(this);
        console.log(`안녕하세요! ${this.name} 입니다.`);
    }
};

const p3: Person = {
    name: 'Mark',
    age: 35,
    hello: (): void => {
        console.log(this);
        console.log(`안녕하세요! ${this.name} 입니다.`);
    }
};

// 각 함수의 scope가 다름. 
p1.hello(); // 안녕하세요! Mark 입니다.
p2.hello(); // 안녕하세요! Mark 입니다.
p3.hello(); // 안녕하세요! 입니다.  // 익명함수의 밖의 부분의 this를 찾음
```

#### class implements interface
```typescript
interface IPerson {
    name: string;
    age?: number;
    hello(): void;
}

class Person implements IPerson {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    hello(): void {
        console.log(`안녕하세요! ${this.name} 입니다.`);
    }
}

const person = new Person('Mark');
person.hello(); // 안녕하세요! Mark 입니다.
```

#### interface extends interface
```typescript
interface Person {
    name: string;
    age?: number;
}

interface Korean extends Person {
    city: string;
}

const k: Korean = {
    name: '이웅재',
    city: '서울'
};
```

#### function interface
```typescript
interface HelloPerson {
    // (name: string, age: number): void;
    (name: string, age?: number): void;
}

let helloPerson: HelloPerson = function (name: string) {
    console.log(`안녕하세요! ${name} 입니다.`);
};

helloPerson('Mark'); // 안녕하세요! Mark 입니다.

/*
함수의 타입 체크는 할당할때가 아니라 사용할때 한다는 점을 명심
*/
```

## Indexable Types

#### string OR number
```typescript
interface StringArray {
    [index: number]: string;
}

const sa: StringArray = {}; // 옵셔널하다
sa[100] = '백';

interface StringDictionary {
    [index: string]: string;
}

const sd: StringDictionary = {}; // 옵셔널하다
sd.hundred = '백';

interface StringArrayDictionary {
    [index: number]: string;
    [index: string]: string;
}

const sad: StringArrayDictionary = {};
// 당연히 옵셔널하다.
sad[100] = '백';
sad.hundred = '백';
```

#### string index = optional property
```typescript
interface StringDictionary {
    [index: string]: string;
    name: string;
}

const sd: StringDictionary = {
    name: '이름' // 필수
};

sd.any = 'any'; // 어떤 프로퍼티도 가능

////////////////////////////////////////////////

interface StringDictionaryNo {
    [index: string]: string;
    // name: number; // (X) 인덱서블 타입이 string 값을 가지기 때문에 number 를 필수로 끌어오면 에러
}
```


## Class

#### 클래스 만들기
```typescript
class Person {
    name: string;
    age: number;
}

const person: Person = new Person();
console.log(person); // Person {}
person.age = 35;
console.log(person.name); // undefined

/*
1. 생성자 함수가 없으면, 디폴트 생성자가 불린다.

2. 클래스의 프로퍼티 혹은 멤버 변수가 정의되어 있지만, 값을 대입하지 않으면 undefined 이다.
=> 오브젝트에 프로퍼티가 아예 존재하지 않는다.

3. 접근제어자 (Access Modifier) 는 public 이 디폴트 이다.
*/
```

#### 클래스와 프로퍼티 (1)
```typescript
class Person {
    name: string;
    age: number;

    constructor() {
        console.log(this.name === null); // false
        console.log(this.name === undefined); // true
    }
}

const person: Person = new Person();
person.name = 'Mark';
person.age = 35;
console.log(person); // Person {name: 'mark', age: 35}
```

#### 클래스와 프로퍼티 (2)
```typescript
class Person {
    name: string = 'Mark';
    age: number = 35;

    constructor() {
        console.log(this.name); // 'mark'
    }
}

const person: Person = new Person();
console.log(person); // Person {name: 'Mark', age: 35}

/*

1. 클래스의 프로퍼티를 선언과 동시에 값을 할당하는 방법도 있다.

2. 생성자가 불리기 전에 이미 프로퍼티의 값이 저장되어 있음을 알 수 있다.
*/
```

#### 클래스와 프로퍼티의 접근 제어자 (1)
```typescript
class Person {
    public name: string;
    private _age: number;

    constructor(age: number) {
        this._age = age;
    }
}

const person: Person = new Person(35);
person.name = 'Mark';
// person._age (X)
console.log(person); // Person {name: 'Mark', _age: 35}

/*
1. private 으로 설정된 프로퍼티는 dot 으로 접근할 수 없다.

2. 클래스 내부에서는 private 프로퍼티를 사용할 수 있다.

3. private 이 붙은 변수나 함수는 _ 를 이름앞에 붙이는데,
이는 문법이 아니라 널리 쓰이는 코딩 컨벤션이다.
*/
```

#### 클래스와 프로퍼티의 접근 제어자 (2)
```typescript
class Parent {
    private privateProp: string;
    protected protectedProp: string;

    constructor() {

    }
}

class Child extends Parent {
    constructor() {
        super();

        this.protectedProp = 'protected';
        // this.privateProp = 'private'; // (X)
    }
}

/*
1. 부모에서 private 으로 설정된 프로퍼티는 상속을 받은 자식에서도 접근할 수 없다.

2. 부모에서 protected 로 설정된 프로퍼티는 상속을 받은 자식에서 접근이 가능하다.

3. 상속을 받은 자식 클래스에서 부모 클래스에 this 를 통해 접근하려면, 생성자에서 super(); 를 통해 초기화 해야한다.
*/
```

#### 클래스와 디폴트 생성자
```typescript
class Person {
    public name: string;
    private _age: number;

    constructor(age: number) {
        this._age = age;
    }
}

const person: Person = new Person();

/*

1. 디폴트 생성자는 프로그래머가 만든 생성자가 없을 때 사용할 수 있다.
=> 사용자가 만든 생성자가 하나라도 있으면, 디폴트 생성자는 사라진다.

*/
```

#### 클래스와 메서드
```typescript
class Person {
    constructor(private _name: string, private _age: number) { }

    print(): void {
        console.log(`이름은 ${this._name} 이고, 나이는 ${this._age} 살 입니다.`);
    }

    printName = (): void => {
        console.log(`이름은 ${this._name} 입니다.`);
    }

    private printAge(): void  {
        console.log(`나이는 ${this._age} 살 입니다.`);
    }
}

const person: Person = new Person('Mark', 35);
person.print(); // 이름은 Mark 이고, 나이는 35 살 입니다.
person.printName(); // 이름은 Mark 입니다.
// person.printAge(); // (X)

/*

1. 클래스 내부에 작성된 메서드는 public 이 디폴트
2. arrow function 으로 작성 가능
3. private 을 이용하면 클래스 외부애서 접근 불가

*/
```

#### 클래스와 상속 (1)
```typescript
class Parent {
    constructor(protected _name: string, protected _age: number) { }

    print(): void {
        console.log(`이름은 ${this._name} 이고, 나이는 ${this._age} 살 입니다.`);
    }

    printName = (): void => {
        console.log(`이름은 ${this._name} 입니다.`);
    }

    private printAge(): void  {
        console.log(`나이는 ${this._age} 살 입니다.`);
    }
}

class Child extends Parent {
    _name = 'Mark Jr.';
}

// const p: Child = new Child(); // (X)
const p: Child = new Child('', 5);
p.print(); // 이름은 Son 이고, 나이는 5 살 입니다.

/*

1. 상속은 extends 키워드를 이용한다.
2. 자식 클래스에서 디폴트 생성자는 부모의 생성자와 입력 형태가 같다.

*/
```

#### 클래스와 상속 (2)
```typescript
class Parent {
    constructor(protected _name: string, private _age: number) { }

    print(): void {
        console.log(`이름은 ${this._name} 이고, 나이는 ${this._age} 살 입니다.`);
    }

    protected printName = (): void => {
        console.log(`이름은 ${this._name} 입니다.`);
    }

    protected printAge(): void  {
        console.log(`나이는 ${this._age} 살 입니다.`);
    }
}

class Child extends Parent {
    constructor(age: number) {
        super('Mark Jr.', age);

        this.printName();
        this.printAge();
    }
}

const p: Child = new Child(1);
// 이름은 Son 입니다.
// 나이는 1 살 입니다.

/*

1. 생성자를 정의하고, this 를 사용하려면, super 를 통해 부모의 생성자를 호출해줘야 한다.
2. super 를 호출할때는 부모 생성자의 입력 타입이 같아야 한다.
3. super 를 호출하는 것은 클래스 외부에서 호출하는 것과 같다.
4. protected 함수를 호출해서 그 안의 private 을 출력하는 것에 주의한다.

*/
```


#### 클래스와 getter, setter
```typescript
class Person {
    private _name: string;
    private _age: number;
    
    constructor(name: string, age: number) {
        this._name = name;
        this._age = age;
     }

    get name() {
        return this._name;
    }

    set name(name: string) {
        // 작업
        this._name = `${name} Lee`;
    }
}

const person: Person = new Person('Mark', 35);

console.log(person.name);
person.name = 'Woongjae';
console.log(person.name);

/*

1. _ 를 변수명 앞에 붙이고, 내부에서만 사용한다.
2. getter 를 함수처럼 설정하면, 프로퍼티처럼 꺼내쓸수있다.
3. 마찬가지로 setter 를 함수처럼 설정하면, 추가 작업을 하고 셋팅할 수 있다.

*/
```

#### 클래스와 static 프로퍼티 => 클래스 멤버 변수
```typescript
class Person {
    public static CITY = "";
    private static lastName: string = 'Lee';
    private _name: string;
    private _age: number;
    
    constructor(name: string, age: number) {
        this._name = name;
        this._age = age;
     }

    public print() {
        console.log(`${this._name} ${Person.lastName} in ${Person.CITY}.`);
    }
}

const person: Person = new Person('Mark', 35);
Person.CITY = 'Seoul';
person.print(); // Mark Lee in Seoul.

/*

1. static 키워드를 붙힌 프로퍼티는 클래스.프로퍼티로 사용한다.
2. static 프로퍼티에 private, protected 를 붙히면 똑같이 동작한다.

*/
```

#### 클래스와 static 메서드 => 클래스 멤버 함수
```typescript
class Person {
    public static Talk(): void {
        console.log('안녕하세요.');
    }
}

Person.Talk(); // 안녕하세요.
```


#### 모듈에서 private static 프로퍼티 혹은 메서드
```typescript
class Person {
    private static PROPERTY = '프라이빗 프로퍼티';
    private static METHOD() {
        console.log('프라이빗 메서드');
    }

    constructor() {
        console.log(Person.PROPERTY);
        Person.METHOD();
    }
}

//////////////////////////////////////////////

const PROPERTY = '모듈 내 변수';
function METHOD() {
    console.log('모듈 내 함수');
}

export class Person {
    constructor() {
        console.log(PROPERTY);
        METHOD();
    }
}
```

#### Abstract Class
```typescript
abstract class APerson {
    protected _name: string = 'Mark';
    abstract setName(name: string): void; 
}

class Person extends APerson {
    setName(name: string): void {
        this._name = name;
    }
}

// const person = new APerson(); // (X)
const person = new Person();

/*
1. abstract 키워드가 사용된 클래스는 new 로 생성할 수 없다.
2. abstract 키워드가 사용된 클래스를 상속하면 abstract 키워드가 붙은 함수를 구현해야 한다.
*/
```


#### Class 와 private constructor
```typescript
class Preference {
    private constructor() {

    }
}

// const p: Preference = new Preference(); (X)

/*
1. 생성자 함수 앞에 접근제어자인 private 을 붙일 수 있다.
2. 외부에서 생성이 불가능하다.
*/
```


#### Class 와 싱글톤 패턴
```typescript
class Preference {
    public static getInstance() {
        if (Preference.instance === null) {
            Preference.instance = new Preference();
        }

        return Preference.instance;
    }
    private static instance: Preference = null;
    private constructor() {

    }
}

const p: Preference = Preference.getInstance();

/*
1. private 생성자를 이용해서 내부에서만 인스턴스 생성이 가능하도록 함.
2. pubilc static 메서드를 통해 private static 인스턴스 레퍼런스를 획득한다.
3. Lazy Loading (Initialization) : 최초 실행시가 아니라, 사용시에 할당을 함
*/
```


#### Class 와 readonly
```typescript
class Person {
    private readonly _name: string = null;
    public readonly age: number = 35;

    constructor(name: string) {
        this._name = name;
    }

    public setName(name: string) {
        // this._name = name; (X)
    }
}

const p: Person = new Person('Mark');
console.log(p.age);
// p.age = 36; // (X)

/*
1. private readonly 로 선언된 경우, 생성자에서는 할당이 가능하다.
2. private readonly 로 선언된 경우, 생성자 이외에서는 할당이 불가능하다.
3. public readonly 로 선언된 경우, 클래스 외부에서는 다른값을 할당할 수 없다.
4. 마치 getter 만 있는 경우와 같다.
*/
```


#### Exercise (1)
```typescript
function Car(name) {
    this.name = name;
    this.speed = 0;
 
    this.honk = function() {
        console.log("부우우웅");
    };
 
    this.accelerate = function(speed) {
        this.speed = this.speed + speed;
    }
}

var car = new Car("BENZ");
car.honk();
console.log(car.speed);
car.accelerate(10);
console.log(car.speed);
```


#### Exercise (2)
```typescript
var baseObject = {
    width: 0,
    length: 0
};

var rectangle = Object.create(baseObject);
rectangle.width = 8;
rectangle.length = 6;
rectangle.area = function() {
    return this.width * this.length;
};

console.log(rectangle.area());
```

#### Exercise (3)
```typescript
var person = {
    _firstName: ""
};

// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty
// ES5 이상
Object.defineProperty(person, "firstName", {
    get: function () {
        return this._firstName;
    },
    set: function (value) {
        if (value.length > 3) {
            this._firstName = value;
        }
        else {
            this._firstName = "";
        }
    },
    enumerable: true,
    configurable: true
});

console.log(person.firstName);
person.firstName = "Ma";
console.log(person.firstName);
person.firstName = "Maximilian";
console.log(person.firstName);
```


## Generic

#### any => generic
```typescript
function helloString(message: string): string {
    return message;
}

function helloNumber(message: number): number {
    return message;
}

// 더 많은 반복된 함수들 ...

function hello(message: any): any {
    return message;
}

function helloGeneric<T>(message: T): T {
    return message;
}

console.log(hello('Mark').length);
console.log(hello(35).length);

console.log(helloGeneric(35).toString()); // console.log(helloGeneric<number>(35).toString());

// hello 의 리턴이 any 이기 때문에 타입 헬퍼가 제대로 되지 않음
// helloGeneric 을 사용하면 정상적으로 사용가능
```

#### basic generic
```typescript
function helloGeneric<T>(message: T): T {
    return message;
}

function hello<T>(message: T): T {
    return message;
}

console.log(hello<string>('Hello'));
let age = hello(35);
hello<number>('35');  // error

/*

1. Generic 타입을 쓰지 않으면, T 로 추론
2. Generic 타입을 쓰면, T 를 확인

*/
```

#### Generic Array
```typescript
function hello<T>(messages: T[]): T {
    return messages[0];
}

console.log(hello<string>(['Hello', 'World']));

/*
hello 함수의 제네릭 타입을 [] 를 이용하여 배열로 사용할 수 있음
*/
```

#### Generic Types
```typescript
type HelloGeneric = <T>(message: T) => T;

const hello: HelloGeneric = <T>(message: T): T => {
    return message;
}

console.log(hello<string>('Hello').length);

/*
구현체에 return T 를 설정하지 않아도,
return false 시 오류가 나지 않는다?
*/
```

#### Generic Class
```typescript
class Person<T> {
    private _name: T;
    private _age: number;

    constructor(name: T) {
        this._name = name;
    }
}

new Person('Mark');
// new Person<string>(35);

/*
명시적으로 제네릭 타입을 설정하면 오류
*/
```

#### Generic with extends
```typescript
class Person<T extends string | number> {
    private _name: T;
    private _age: T;

    constructor(name: T) {
        this._name = name;
    }
}

new Person('Mark');
new Person(35);
// new Person(true);

/*
T 가 string 또는 number 를 상속받기 때문에 boolean 은 안된다.
*/
```

#### Generic with multiple types
```typescript
class Person<T, K> {
    private _name: T;
    private _age: K;

    constructor(name: T, age: K) {
        this._name = name;
        this._age = age;
    }
}

new Person('Mark', 35);
```

#### type lookup system
```typescript
interface Person {
    name: string;
    age: number;
}

const person: Person = {
    name: 'Mark',
    age: 35
};

function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

function setProperty<T, K extends keyof T>(obj: T, key: K, value: T[K]): void {
    obj[key] = value;
}

console.log(getProperty(person, 'name'));
// console.log(getProperty(person, fullname));
setProperty(person, 'name', 'Anna');
console.log(getProperty(person, 'name'));
// setProperty(person, 'name', 24);
```


## Iterator
- for..of
- es3
  - for (var i = 0; i < array.length; i++)
- es5
  - array.forEach
  - return 으로 순회를 탈출할 수 없다.
- es6
  - for (const item of array)
  - 배열에서만 사용이 가능

- for..in
  - 배열을 순회할 때는 사용하지 않을 것
  - index 가 number 가 아니라 string 으로 나온다.
  - 배열의 프로퍼티를 순회할 수도 있다.
  - prototype 체인의 프로퍼티를 순회할 수도 있다.
- 루프가 무작위로 순회할 수도 있다.
  - for..of 를 쓸 것
  - 객체를 순회할 때
  - for (const prop of Object.keys(obj)) 도 사용할 수 있다.

#### Example
```typescript
const array = ['first', 'second'];
const obj = {
    name: 'Mark',
    age: 35
};

// 배열에 for..of 이용
for (const item of array) {
    console.log(typeof item + ', ' + item);
}

// 배열에 for..in 이용
// item 이 string 타입의 숫자
for (const item in array) {
    console.log(typeof item + ', ' + item);
}


// 객체에 for..of 이용 => 오류
/*
for (const item of obj) {
    console.log(typeof item + ', ' + item);
}
*/

// 객체에 for..in 이용
for (const item in obj) {
    console.log(typeof item + ', ' + item);
}

// 객체의 keys 들에 for..of 이용
for (const item of Object.keys(obj)) {
    console.log(typeof item + ', ' + item);
}
```

#### target es3 forEach
```typescript
const array = ['first', 'second'];

// ts
array.forEach((item) => {
    console.log(item);
});

// js
array.forEach(function (item) {
    console.log(item);
});

/*

target 이 es3 인데도 forEach 는 트랜스파일이 되지 않았음.
https://github.com/Microsoft/TypeScript/issues/2410

*/
```

#### Symbol.iterator
- 프로퍼티이며, 함수가 구현되어있으면, iterable 이라고 한다.
- Array, Map, Set, String, Int32Array, Uint32Array, etc. 에는 내장된 구현체가 있으므로 이터러블 하다.
- 그냥 객체는 이터러블하지 않다.
- 이터레이터를 통해 이터러블한 객체의 Symbol.iterator 함수를 호출한다.
- [http://slides.com/woongjae/typescript-basic#/13/5](http://slides.com/woongjae/typescript-basic#/13/5)

- target : es3 or es5
  - Array 에만 for..of 사용 가능
  - 일반 객체에 사용하면 오류
- target : es6
  - Symbol.iterator 함수를 구현하면 어떤 객체에도 for..of 사용 가능


#### lib.es6.d.ts
```typescript
interface IteratorResult<T> {
    done: boolean;
    value: T;
}

interface Iterator<T> {
    next(value?: any): IteratorResult<T>;
    return?(value?: any): IteratorResult<T>;
    throw?(e?: any): IteratorResult<T>;
}

interface Iterable<T> {
    [Symbol.iterator](): Iterator<T>;
}

interface IterableIterator<T> extends Iterator<T> {
    [Symbol.iterator](): IterableIterator<T>;
}
```

#### Custom Iterable
```typescript
class CustomIterable implements Iterable<string> {
    private _array: Array<string> = ['first', 'second'];

    [Symbol.iterator]() {
        var nextIndex = 0;

        return {
            next: () => {
                return {
                    value: this._array[nextIndex++],
                    done: nextIndex > this._array.length
                }
            }
        }
    }
}

const cIterable = new CustomIterable();

for (const item of cIterable) {
    console.log(item);
}
```


## decorator

#### Decorator 종류
- Class Decorator
- Method Decorator
- Property Decorator
- Parameter Decorator

#### Decorator 코드 작성 준비

step1. 프로젝트 생성

```bash
$ mkdir ts-decorator
$ cd ts-decorator
$ yarn init -y
```
step2. typescript 설치

```bash
$ yarn add typescript -D
```

step3. tsconfig 설정
```bash
$ node_modules/.bin/tsc --init
# experimentalDecorators 추가
```
​step4. vscode 컴파일 설정

```bash
$ ${workspaceRoot}/node_modules/.bin/tsc
$ command + shift + <B>
```

#### Class Decorator Basic
```typescript
function hello(constructorFn: Function) {
    console.log(constructorFn);

    // AOP 개념
    constructorFn.prototype.test = function () {
      console.log(test);
    }
}

function helloFactory(show: boolean) {
    if (show) {
        return hello;
    } else {
        return null;
    }
}

// @hello
@helloFactory(true)
class Person {
    constructor() {
        console.log('new Person()');
    }
}

const p = new Person();

// 힌트는 뜨지 않는다. 에러가 원래 뜨지만 as any로 잡아줌.
(p as any).test();
/*
helloFactory 는 팩토리 스타일
*/
```


#### Class Decorator Advanced
```typescript
function addHello(constructorFn: Function) {
    constructorFn.prototype.hello = function() {
        console.log('hello');
    }
}

@addHello
class Person {
    constructor() {
        console.log('new Person()');
    }
}

const person = new Person();
(<any>person).hello();
```

#### Method Decorator
```typescript
function editable(canBeEdit: boolean) {

    return function(target: any, propName: string, description: PropertyDescriptor) {
        console.log(canBeEdit);
        console.log(target);
        console.log(propName);
        console.log(description);
        description.writable = canBeEdit;
    }
}

class Person {
    constructor() {
        console.log('new Person()');
    }

    @editable(true)
    hello() {
        console.log('hello');
    }
}

const person = new Person();
person.hello();
person.hello = function() {
    console.log('world');
}
person.hello();
```


#### Property Decorator
```typescript
function writable(canBeWrite: boolean) {
    return function(target: any, propName: string): any {
        console.log(canBeWrite);
        console.log(target);
        console.log(propName);
        return {
            writable: canBeWrite
        }
    }
}

class Person {
    @writable(false)
    name: string = 'Mark';

    constructor() {
        console.log('new Person()');
    }
}

const person = new Person();
console.log(person.name);

/*
undefined
*/
```

#### Parameter Decorator
```typescript
function printInfo(target: any, methodName: string, paramIndex: number) {
    console.log(target);
    console.log(methodName);
    console.log(paramIndex);
}

class Person {
    private _name: string;
    private _age: number;

    constructor(name: string, @printInfo age: number) {
        this._name = name;
        this._age = age;
    }

    hello(@printInfo message: string) {
        console.log(message);
    }
}

/*
Person { hello: [Function] }
hello
0
[Function: Person]
undefined
1
*/
```

#### DI Framework [http://inversify.io/](http://inversify.io/)

#### reflect-metadata 확인해보기


## Type Inference

#### 타입 추론
- 기본적으로 타입을 명시적으로 쓰지 않을 때 추론하는 방법에 대한 규칙
  - 명시적으로 쓰는 것은 타입 추론이 아니라 코드를 읽기 좋게 하는 지름길
- let 은 기본적으로 우리가 아는 기본 자료형으로 추론
- const 는 리터럴 타입으로 추론
  - 오브젝트 타입을 타입을 쓰지 않으면, 프로퍼티는 let 처럼 추론
  -  const person = {name: 'Mark', age: 35}; 면
  -  person => {name: string; age: number;} 로 추론
- 대부분은 추론이 쉽다.
  - 단순 변수
  - structuring, destructuring
- array, 함수의 리턴에서는 원하는데로 얻기가 힘들다.

#### 배열 타입 추론
```typescript
const array1 = [];  // any
const array2 = ['a', 'b', 'c']; //string
const array3 = ['a', 1, false]; // string | number | boolean

class Animal {
    name: string;
}

class Dog extends Animal { 
    dog: string;
}

class Cat extends Animal {
    cat: string;
}

const array4 = [new Dog(), new Cat()];  // Dog | Cat
```

#### 리턴 타입 추론
```typescript
// 'world' | 0
function hello(message: string | number) {
    if (message === 'world') {
        return 'world';
    } else {
        return 0;
    }
}
```

#### 유니온 타입과 타입 가드  중요!
```typescript
interface Person {
    name: string;
    age: number;
}

interface Car {
    brand: string;
    wheel: number;
}

function isPerson(arg: any): arg is Person {  // 리턴은 Person이다
    return arg.name !== undefined;
}

function hello(arg: Person | Car) {
    if (isPerson(arg)) {
        console.log(arg.name);
        // console.log(arg.brand);
    } else {
        // console.log(arg.name);
        console.log(arg.brand);
    }
}
```

## Road Map

[https://github.com/Microsoft/TypeScript/wiki/Roadmap](https://github.com/Microsoft/TypeScript/wiki/Roadmap)


