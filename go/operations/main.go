package main

import "fmt"

const (
	const1 uint8 = 1 << iota
	const2
	const3
)

func main() {
	fmt.Printf("%08b\n", const1)
	fmt.Printf("%08b\n", const2)
	fmt.Printf("%08b\n", const3)
	/**
	  00000001
	  00000010
	  00000100
	*/
}
