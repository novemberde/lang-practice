package main

import (
	"os"
	"text/template"
)

func main() {
	const templ = `
		Number: n0 = {{.n0}}
		Number: n1 = {{printf "%.2f" .n1}}
	`
	tt, _ := template.New("").Parse(templ)
	tt.Execute(os.Stdout, map[string]float64{
		"n0": 10000000000.77,
		"n1": 10000000000.66,
	})
}
