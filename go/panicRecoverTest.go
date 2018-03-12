package main

import "fmt"

func main() {
	defer func() {
		s:= recover()

		fmt.Println(s)
	}()

	panic("Error!!")
}