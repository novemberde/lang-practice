package main

import (
	"fmt"
)

func main() {
	fmt.Println(sum1(1, 2))
	fmt.Println(sum2(1, 2))
	fmt.Println(sumAndSub(1, 2))
	fmt.Println(sum3(1, 2, 3, 4, 5))
	fmt.Println(factorial(10))
	func () {
		fmt.Println("hello!")
	} ()

	a := func(a string, b string) string {
		return a + b
	} ("Hello ", "World!")
	fmt.Println(a)
}

func sum1(a int, b int) (result int) {
	result = a + b
	return
}
func sum2(a int, b int) int {
	return a + b
}
func sumAndSub(a int, b int) (int, int) {
	return a + b, a - b
}
func sum3(n ...int) int {
	total := 0
	for _, value := range(n) {
		total += value
	}

	return total
}
func factorial(n uint64) uint64 {
	if n==0 {
		return 1
	}

	return n * factorial(n-1)
}