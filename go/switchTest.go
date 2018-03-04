package main

import (
	"fmt"
)

func main() {
	for i := 0; i < 5; i++ {
		switch i {
		case 3:
			fmt.Println(i)
			break
		case 4:
			fmt.Println(i)
			fallthrough
		default:
			fmt.Println("default")
		}
	}
}
