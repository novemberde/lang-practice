package main

import "fmt"

func main() {
	fmt.Println("Hello, world")
	
	i := 10
	
	if i>=5 {
	    fmt.Println("Five or more")
	}
	
	for i:=0; i<5; i++ {
	    fmt.Println(i)
	}
}

// go build hello
// in linux and mac, execute file is "hello". In widows, execute file is "hello.exe"
