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
			if char == "X" {
				if j+3 < len(lines[0]) && lines[i][j+1] == "M" && lines[i][j+2] == "A" && lines[i][j+3] == "S" {
					count += 1
				}
				if i+3 < len(lines) && lines[i+1][j] == "M" && lines[i+2][j] == "A" && lines[i+3][j] == "S" {
					count += 1
				}
				if j+3 < len(lines[0]) && i+3 < len(lines) && lines[i+1][j+1] == "M" && lines[i+2][j+2] == "A" && lines[i+3][j+3] == "S" {
					count += 1
				}
				if j+3 < len(lines[0]) && i-3 >= 0 && lines[i-1][j+1] == "M" && lines[i-2][j+2] == "A" && lines[i-3][j+3] == "S" {
					count += 1
				}
			} else if char == "S" {
				if j+3 < len(lines[0]) && lines[i][j+1] == "A" && lines[i][j+2] == "M" && lines[i][j+3] == "X" {
					count += 1
				}
				if i+3 < len(lines) && lines[i+1][j] == "A" && lines[i+2][j] == "M" && lines[i+3][j] == "X" {
					count += 1
				}
				if j+3 < len(lines[0]) && i+3 < len(lines) && lines[i+1][j+1] == "A" && lines[i+2][j+2] == "M" && lines[i+3][j+3] == "X" {
					count += 1
				}
				if j+3 < len(lines[0]) && i-3 >= 0 && lines[i-1][j+1] == "A" && lines[i-2][j+2] == "M" && lines[i-3][j+3] == "X" {
					count += 1
				}
			}
		}
	}
	fmt.Println(count)
}
