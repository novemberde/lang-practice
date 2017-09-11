import * as fs from 'fs';
import * as request from 'superagent'; //타입이없음.

class Person {
  private _name = "Mark";

  great () {
    console.log("Yeah");
  }
}

const p = new Person();

const a = 1;

// can not be accessible
// p._name;