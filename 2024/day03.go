package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/yodigi7/advent-of-code/utils"
)

func reverseString(s string) string {
	// Convert string to a slice of runes to handle multi-byte characters correctly
	runes := []rune(s)

	// Reverse the rune slice
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	// Convert the reversed rune slice back to a string
	return string(runes)
}

func getResults(str string) int {
	re := regexp.MustCompile(`mul\((-?\d+),(-?\d+)\)`)
	matches := re.FindAllStringSubmatch(str, -1)
	result := 0
	for _, match := range matches {
		num1, err1 := strconv.Atoi(match[1])
		num2, err2 := strconv.Atoi(match[2])
		if err1 != nil {
			fmt.Println(err1)
			continue
		}
		if err2 != nil {
			fmt.Println(err2)
			continue
		}

		// fmt.Println(num1)
		// fmt.Println(num2)
		result += num1 * num2
	}
	return result
}

func main() {
	lines, err := utils.ReadFileLines("day03.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	result := 0
	re2 := regexp.MustCompile(`^(.*?)don't\(\)`)
	re3 := regexp.MustCompile(`do\(\)(.*?)don't\(\)`)
	// Calculate the last section of do() to EOF, checked manually in my input file and it requires it
	re4 := regexp.MustCompile(`^(.*?)\)\(od`)
	lastSection := 0
	first := true
	for _, line := range lines {
		if first {
			matches := re2.FindAllStringSubmatch(line, -1)
			result += getResults(matches[0][1])
			first = false
		}
		locs := re3.FindAllStringIndex(line, -1)
		for _, loc := range locs {
			result += getResults(line[loc[0]:loc[1]])
		}
		matches := re4.FindAllStringSubmatch(reverseString(line), -1)
		for _, match := range matches {
			lastSection = getResults(reverseString(match[1]))
			fmt.Println(lastSection)
		}
	}
	result += lastSection
	fmt.Println(result)
}
