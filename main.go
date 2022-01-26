package main

import "fmt"

func summation(num1 int, num2 int) int {
	return num1 + num2
}

func concat(str1 string, str2 string) string {
	return str1 + str2
}

func main() {
	sum := summation("hello", "world")

	fmt.Println(sum)
}
