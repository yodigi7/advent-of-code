package main

import (
	"fmt"
	"github.com/yodigi7/advent-of-code/utils"
)

func isDescending(r []int) bool {
	firstVal := true
	prevVal := 0
	for _, val := range r {
		if firstVal {
			firstVal = false
			prevVal = val
			continue
		}
		diff := prevVal - val
		prevVal = val
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func isAscending(r []int) bool {
	firstVal := true
	prevVal := 0
	for _, val := range r {
		if firstVal {
			firstVal = false
			prevVal = val
			continue
		}
		diff := val - prevVal
		prevVal = val
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func isSafe(r []int) bool {
	return isAscending(r) || isDescending(r)
}

func main() {
	lines, err := utils.ReadFileListOfInts("day02.txt")
	if err != nil {
		fmt.Println(err)
	}
	count := 0
	for _, row := range lines {
		if isSafe(row) {
			count += 1
		} else {
			for i := range row {
				copyRow := make([]int, len(row))
				copy(copyRow, row)
				if isSafe(append(copyRow[:i], copyRow[i+1:]...)) {
					count += 1
					break
				}
			}
		}
	}
	fmt.Println(count)
}
