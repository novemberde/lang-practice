package main

import (
	"fmt"
	"io/ioutil"
)

func main () {
	// b, err := ioutil.ReadFile("./README.md")
	// if err == nil {
	// 	fmt.Println("%s", b)
	// }
	if b,err := ioutil.ReadFile("./READM.md"); err==nil {
		fmt.Printf("%s", b)
	} else {
		fmt.Printf("%s", err)
	}
}