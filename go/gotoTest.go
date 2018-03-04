package main

import (
	"fmt"
)

func main()  {
	var a int = 1

	if a==1 {
		goto ERROR1
	} else if a==2 {
		goto ERROR2
	}

	fmt.Println(a)
	fmt.Println("success")

	ERROR1:
		a++
		fmt.Println("Error1")
		return;

	ERROR2:
		fmt.Println("Error2")
		return;
}

