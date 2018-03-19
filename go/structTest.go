package main

import (
	"fmt"
)

type Rectangle struct {
	// width, height int
	width int
	height int
}

func NewRectangle(width, height int) *Rectangle {
	return &Rectangle{width, height}
}

func rectangleArea (rect *Rectangle) int {
	return rect.width * rect.height
}

func (rect *Rectangle) area() int {
	return rect.width * rect.height
}

func (rect Rectangle) scaleA (factor int) {	// Call by reference
	rect.width = rect.width * factor
	rect.height = rect.height * factor
}
func (rect *Rectangle) scaleB (factor int) {		// Call by value
	rect.width = rect.width * factor
	rect.height = rect.height * factor
}
func (_ Rectangle) hello () {
	fmt.Println("Hello from rectangle")
}

func main() {
	var rect1 Rectangle
	var rect2 *Rectangle = new(Rectangle)
	rect3 := NewRectangle(10,20)
	rect4 := &Rectangle{20,50}

	rect1.width = 20
	rect2.width = 30

	fmt.Println(rect1)
	fmt.Println(rect2)
	fmt.Println(rect3)
	fmt.Println(rect4)
	fmt.Println(rectangleArea(rect3))
	fmt.Println(rect4.area())
	rect4.scaleA(2)
	fmt.Println(rect4)	//&{20 50}
	rect4.scaleB(2)
	fmt.Println(rect4)	//&{40 100}
	rect1.hello()
}