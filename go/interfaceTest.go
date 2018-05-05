package main

import "fmt"

type hello interface {}

type MyInt int

func (i MyInt) Print() {
	fmt.Println(i)
}

type Printer interface {
	Print()
}

func main() {
	var h hello
	fmt.Println(h)	// nil

	var i MyInt = 5
	var p Printer

	p = i
	p.Print()
}