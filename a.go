package main

import "unicode/utf8"

func main() {
	var TmpStr = "HEllp 你好"
	println(len(TmpStr))
	println("utf8:", utf8.RuneCountInString(TmpStr))
	print("utf82:", len([]rune(TmpStr)))
}
