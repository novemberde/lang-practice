package main

import (
	"context"
	"fmt"
	"time"

	"golang.org/x/sync/semaphore"
)

func main() {
	ctx, cancel := context.WithTimeout(context.TODO(), time.Second*2)
	defer cancel()

	sema := semaphore.NewWeighted(2)
	for i := 0; i < 10; i++ {
		sema.Acquire(ctx, 1)
		a := i
		fmt.Printf("a : %d\n", a)
		go func() {
			defer sema.Release(1)

			<-time.After(time.Second)
			fmt.Println(a)
		}()
	}
	sema.Acquire(ctx, 2)
}
