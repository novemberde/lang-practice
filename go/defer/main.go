package main

import "fmt"

func main() {
	a := 1
	fmt.Println("1: ", a)

	defer fmt.Println("2: ", a)

	a++
	fmt.Println("3: ", a)
}
