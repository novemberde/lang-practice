package main

import (
	"fmt"
)

// Create a new type of 'deck'
// which is a slice of strings
type deck []string

func (d deck) print() {
	// go lang don't use this or self like python or javascript.
	// Usually variable name is single or three letter.
	for i, card := range d {
		fmt.Println(i, card)
	}
}

// func (d deck) println() {
// 	for i, card := range d {
// 		fmt.Println(i, card)
// 		fmt.Println()
// 	}
// }
