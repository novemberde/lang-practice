package main

// import "fmt"
import "os/exec"

import "log"

func main() {
	cmd := exec.Command("/bin/sh", "ls")
	// 	stdout, err := cmd.StdoutPipe()
	// 	log.Fatal(err)
	// 	fmt.Println(stdout)
	err := cmd.Run()
	log.Fatal(err)
}
