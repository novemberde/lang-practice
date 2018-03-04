package main

import (
	"fmt"
	"runtime"
)

func main () {
	fmt.Println("CPU count: ", runtime.NumCPU())
}