package main

import (
	"fmt"
)

func main() {
	// var card string = "Ace of Spades"
	// card := "Ace of Spades"
	// fmt.Println(card)
	// card = "Five of Diamonds"
	// fmt.Println(card)

	// This is not available
	// card := "Five of Diamonds"

	// card := newCard()
	// fmt.Println(card)

	// // slides of type string
	// cards := []string{"Ace of Diamonds", newCard()}
	// cards = append(cards, "Six of Spades")
	// fmt.Println(cards)

	// // i: index of this element in the array
	// // card: Current card we're iterating over
	// // range cards: Take the slice of 'cards' and loop over it
	// for i, card := range cards {
	// 	fmt.Println(i, card)
	// }

	// cards := deck{"Ace of Diamonds", newCard()}
	// cards = append(cards, "Six of Spades")

	// cards.print()

	// cards := newDeck()
	// cards.print()

	// cards := newDeck()
	// hand, remainingDeck := deal(cards, 5)

	// hand.print()
	// remainingDeck.print()

	// greeting := "Hi there!"
	// fmt.Println([]byte(greeting)) // [72 105 32 116 104 101 114 101 33]

	cards := newDeck()
	fmt.Println(cards.toString())
}

// func newCard() string {
// 	return "Five of Diamonds"
// }
