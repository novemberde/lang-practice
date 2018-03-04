package main

import (
	"fmt"
)

func main() {
	var a map[string]int = make(map[string]int)	// key string, value int
	b := make(map[string]int)

	a["hello"] = 1
	a["world"] = 2

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(a["hello"])

	for k,v:= range(a) {
		fmt.Println(k, v)
	}

	delete(a, "hello")

	fmt.Println(a)

	c := map[string]map[string]map[string]string{}

	c["aaa"] = map[string]map[string]string{
		"bbb": map[string]string{
			"ccc": "ddd",
		},
	}

	fmt.Println(c)
}