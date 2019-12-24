package main

import "fmt"

func main() {
	c := make(chan string)

	for i := 0; i < 1000000; i++ {
		go asyncHello(c)
	}

	fmt.Println(<-c)
	fmt.Println(<-c)
	fmt.Println("hello")
}

func asyncHello(a chan string) {
	a <- "hi"
}
