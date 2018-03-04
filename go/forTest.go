package main

import (
	"fmt"
)

func main ()  {
	for i:=0; i<3; i++ {
		fmt.Println(i)
	}

	// infinite for loop 
	// for {
	// 	fmt.Println("hi");
	// }

	i:=0
	for i<3 {
		fmt.Println(i)
		i++
	}

	fmt.Println("\n")
	Loop1:
		for i:=0; i<3; i++ {
			for j:=0; j<2; j++ {
				
				if i==2 {
					break Loop1
				} else if i==1 {
					continue Loop1
				}

				fmt.Println(i, j)
			}
		}

}