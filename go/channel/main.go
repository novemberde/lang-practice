package main

import (
	"fmt"
)

func main() {

	// ctx, cancel := context.WithTimeout(context.TODO(), time.Second*3)
	// defer cancel()
	// ch := make(chan struct{})
	// go func() {
	// 	<-time.After(time.Second)
	// 	<-ch
	// 	log.Debug().Msg("hi5")
	// }()

	// select {
	// case ch <- struct{}{}:
	// 	log.Debug().Msg("hi")
	// case <-ctx.Done():
	// 	log.Debug().Msg("hi2")
	// }

	// select {
	// case <-ch:
	// 	log.Debug().Msg("hi3")
	// default:
	// 	log.Debug().Msg("hi4")
	// }
	for i := 0; i < 3; i++ {
		fmt.Println("hi", i)
		defer fmt.Println("bye", i)
	}
}
