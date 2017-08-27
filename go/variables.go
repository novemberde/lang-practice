package main

import "fmt"

var i int
var s string
var age int = 10
var name string = "name"

// var address // occur an error
// a := "a"    // occur an error. can not be declared on here.

var b, c string = "b", "c"

func main() {
	a := "a"

	fmt.Println("hi") // hi
	fmt.Println(name) // name
	fmt.Println(a)    // a
}
