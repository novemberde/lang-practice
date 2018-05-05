package main

import (
	"fmt"
)

type Person struct {
	name string
	age int
}

func (p *Person) greeting() {
	fmt.Println("Hello")
}

type Student struct {
	p Person	// Has-a 
	school string
	grade int
}

type Student2 struct {
	Person // Is-a	// anonymous field
	school string
	grade int
}

// Override
func (s Student2) greeting() {
	fmt.Println("Hello2")
}

func main() {
	var s Student
	var s2 Student2

	s.p.greeting()
	s2.greeting()
}
