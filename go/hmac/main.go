package main

import (
	"crypto/hmac"
	"crypto/sha1"
	"log"
)

func main() {
	bytes := []byte("{\"a\": 123}")
	mac := hmac.New(sha1.New, []byte("abcd"))
	log.Println(string(mac.Sum(bytes)))
	log.Println()
	mac.Write(bytes)
	log.Println()
	log.Println(string(mac.Sum(nil)))
}
