package main

import "fmt"

func main() {
	defer func() {
		// This cannot be call
		fmt.Println("hello")
		if r := recover(); r != nil {
			fmt.Println(r)
		}
	}()
	m := map[string]int{}
	go func() {
		for {
			m["x"] = 1
		}
	}()
	for {
		_ = m["x"]
	}
}
