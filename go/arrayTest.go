package main

import (
	"fmt"
)

func main () {
	var a [5]int
	a[2] = 7

	fmt.Println(a)

	var b [5]int = [5]int{32,29,1,2,3}
	var c = [5]int{1,2,3,4,5}
	d := [5]int{1,2,3,4,5}

	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)

	for i:=0; i<len(b); i++ {
		fmt.Println(b[i])
	}
	for i,bb := range b {
		fmt.Println(i, bb)
	}
	for _,cc := range c {
		fmt.Println(cc)
	}
}