package main

import (
	"fmt"
)

func main () {
	var a []int

	a = make([]int, 5)

	var b = make([]int, 5)
	c := make([]int, 5, 10)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)

	d:= []int{1,2,3,4,5}
	e:= []int{
		1,
		2,
		3,
	}

	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(len(d))
	fmt.Println(cap(c))
	fmt.Println(cap(e))

	f := append(e, 1,2,3,4)
	fmt.Println(f)


	// Slice compare to Array
	// Call by value
	g := [3]int{1,2,3}
	h := g
	h[0] = 10
	fmt.Println(g) 
	fmt.Println(h)

	// Call by reference
	i := []int{1,2,3}
	j := i
	j[0] = 10
	fmt.Println(i) 
	fmt.Println(j)

	k := []int{1,2,3,4,5,6,7,8}
	l := k[0:3:8]
	fmt.Println(l) // [1 2 3]
	fmt.Println(len(l), cap(l)) // 3 8
} 