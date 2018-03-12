package main

import (
	"fmt"
)

func main() {
	sum := func(a, b int) int {
		return a + b
	}

	r := sum(1, 2)

	fmt.Println(r)

	a, b := 3, 5
	f := func(x int) int {
		return a*x + b
	}
	y := f(5)

	fmt.Println(y)

	z := calc()(2)
	fmt.Println(z)
}

func calc() func(x int) int {
	a, b := 3, 5
	return func(x int) int {
		return a*x + b
	}
}
