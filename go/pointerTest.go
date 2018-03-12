package main

import "fmt"

func main () {
	var numPtr *int // 포인터형 변수는 nil로 초기화
	fmt.Println(numPtr)		// <nil>

	numPtr = new(int)	// 메모리 주소를 할당
	fmt.Println(numPtr)		// 0xc420016098

	// 역참조로 포인터에 변수를 대입
	*numPtr = 1
	fmt.Println(*numPtr)	// 1

	num := 2
	numPtr = &num // 참조로 num변수의 메모리 주소를 구하여 numPtr에 포인터 변수 대입
	fmt.Println(*numPtr)	// 2
	fmt.Println(numPtr)		// 0xc4200160b8
	fmt.Println(numPtr)		// 0xc4200160b8

	// go에서는 메모리 주소를 직접 대입하거나 포인터 연산을 허용하지 않는다.
	// numPtr++					// Error
	// numPtr = 0xc420016098	// Error

	changReference(&num)
	fmt.Println(num)		// 3
}

func changReference (n *int) {
	*n = 3
}