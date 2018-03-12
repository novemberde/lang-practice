package main

import (
	"fmt"
	"os"
)

func hi() {
	fmt.Println("hi")
}

func hihi() {
	fmt.Println("hihi")
}

func hihihi() {
	defer func() {
		fmt.Println("hihihi")
	}()
	hi();
}

func main() {
	defer hihi()	// main함수 끝나기 전에 호출
	hi()
	hi()
	hi()
	fmt.Println("\n")
	hihihi()

	ReadFile()
}

func ReadFile() {
	file, err := os.Open("README.md")
	defer file.Close()	// 마지막에 호출됨

	if err != nil {
		fmt.Println(err)
		return	// call file.Close 
	}

	buf := make([]byte, 100)
	if _,err = file.Read(buf); err != nil {
		fmt.Println(err)x
		return	// call file.Close 
	}

	fmt.Println(string(buf))
	// call file.Close 
}