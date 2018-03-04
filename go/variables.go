package main

import (
	"fmt"
	"math"
)

var i int
var s string
var age int = 10
var name string = "name"

// var address // occur an error
// a := "a"    // occur an error. can not be declared on here.

var b, c string = "b", "c"

func main() {
	// a := "a"

	fmt.Println("hi") // hi
	fmt.Println(name) // name
	// fmt.Println(a)    // a

	var num1 float32 = 0.1
	var num2 float32 = .35
	var num3 float32 = 123.123
	var num4 float64 = 5.123123e-10
	var num5 float64 = 1e7
	var num6 float64 = .1234E+2


	fmt.Println(num1)
	fmt.Println(num2)
	fmt.Println(num3)
	fmt.Println(num4)
	fmt.Println(num5)
	fmt.Println(num6)

	var a float64 = 10.0

	for i:=0; i<10; i++ {
		a = a - 0.1
	}

	fmt.Println(a)	//9.000000000000004

	const epsilon = 1e-14;	// Go 언어 머신 엡실론
	fmt.Println(math.Abs(a-9.0) <= epsilon)

	const (
		enum1 = 0
		enum2 = 1
		enum3 = 2
	)
	const (
		enum4 = iota
		enum5
		enum6
	)

	fmt.Println(enum1, enum2, enum3, enum4, enum5, enum6)
}
