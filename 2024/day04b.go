package main

import (
	"fmt"

	"github.com/yodigi7/advent-of-code/utils"
)

func main() {
	lines, err := utils.ReadFileCharByChar("day04.txt")
	if err != nil {
		fmt.Println(err)
	}

	count := 0
	for i, line := range lines {
		for j, char := range line {
			if j+2 < len(line) && i+2 < len(lines) && lines[i+1][j+1] == "A" {
				if char == "M" {
					if lines[i+2][j] == "M" && lines[i][j+2] == "S" && lines[i+2][j+2] == "S" {
						count += 1
					}
					if lines[i+2][j] == "S" && lines[i][j+2] == "M" && lines[i+2][j+2] == "S" {
						count += 1
					}
				} else if char == "S" {
					if lines[i+2][j] == "M" && lines[i][j+2] == "S" && lines[i+2][j+2] == "M" {
						count += 1
					}
					if lines[i+2][j] == "S" && lines[i][j+2] == "M" && lines[i+2][j+2] == "M" {
						count += 1
					}
				}
			}
		}
	}
	fmt.Println(count)
}
