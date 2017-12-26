# Go cli

- go build: Compiles a bunch of go source code files
- go run: Compiles and executes one or two files
- go fmt: Formats all the code in each file in the current directory
- go install: Compiles and installs a package
- go get: Downloads the raw source code of someone else's pakage
- go test: Runs any tests associated with the current project


# What does 'package main mean?'

Package == Project == Workspace

Types of Packages

- Executable: Generates a file that we can run
- Reusable: Code used as 'helpers'. Goo place to put reusable logic. For example, Libraries.

1. package main -> go build -> main.exe(If we ran this file, the fucntion named 'main' would be automatically ran)
2. package blahblah -> go build -> nothing!(Compiling a non-main package gives)

How it works?

1. package main: Defines a package that can be compiled and then executed. Must have a func called 'main' --- Executable packager
2. package calculator: Defines a package that can be used as a dependency(helper code) --- Reusable package
3. pakcage uploader: Defines a package that can be used as a dependency(helper code) --- Reusable package


# What does 'import "fmt"' mean?

- math
- debug
- encoding
- main
- fmt
- crypto
- io

- main
    - fmt: Standard lib
    - calculator: Reusable package
    - uploader: Reusable package

golang.org/pkg

