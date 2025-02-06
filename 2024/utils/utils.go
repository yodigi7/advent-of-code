package utils

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func ReadFileCharByChar(filename string) ([][]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var result [][]string
	var currentRow []string

	reader := bufio.NewReader(file)
	for {
		char, _, err := reader.ReadRune()
		if err != nil {
			if err.Error() == "EOF" { // Handle EOF properly
				break
			}
			return nil, err // Return actual errors
		}

		if char == '\n' {
			if len(currentRow) > 0 { // Avoid adding empty rows from consecutive newlines
				result = append(result, currentRow)
				currentRow = nil
			}
		} else if char != '\r' { // Ignore carriage return
			currentRow = append(currentRow, string(char))
		}
	}

	// Append the last row if it contains any data
	if len(currentRow) > 0 {
		result = append(result, currentRow)
	}

	return result, nil
}

// func ReadFileCharByChar(filename string) ([][]string, error) {
// 	file, err := os.Open(filename)
// 	if err != nil {
// 		return nil, err
// 	}
// 	defer file.Close()

// 	var result [][]string
// 	var currentRow []string

// 	// Using bufio.Reader to read one character at a time
// 	reader := bufio.NewReader(file)
// 	for {
// 		char, _, err := reader.ReadRune() // Read one rune (character)
// 		if err != nil {
// 			break
// 		}

// 		// Example logic: when the character is a newline, start a new row
// 		if char == '\n' {
// 			result = append(result, currentRow) // Append the current row
// 			currentRow = nil                    // Reset the current row
// 		} else {
// 			currentRow = append(currentRow, string(char)) // Add the character to the row
// 		}
// 	}

// 	// Add the last row if any
// 	if len(currentRow) > 0 {
// 		result = append(result, currentRow)
// 	}

// 	return result, nil
// }

// ReadFileLines reads a file and returns its lines as a slice of strings
func ReadFileLines(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

// ReadFileInts reads a file and converts each line to an integer
func ReadFileInts(filename string) ([]int, error) {
	lines, err := ReadFileLines(filename)
	if err != nil {
		return nil, err
	}

	var nums []int
	for _, line := range lines {
		num, err := strconv.Atoi(line)
		if err != nil {
			return nil, err
		}
		nums = append(nums, num)
	}
	return nums, nil
}

// ReadFileInts reads a file and converts each line to an integer
func ReadFileListOfInts(filename string) ([][]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var result [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.TrimSpace(line) == "" {
			continue // Skip empty lines
		}

		numStrs := strings.Fields(line) // Split by whitespace
		var numbers []int
		for _, numStr := range numStrs {
			num, err := strconv.Atoi(numStr)
			if err != nil {
				return nil, err // Return error if conversion fails
			}
			numbers = append(numbers, num)
		}

		result = append(result, numbers)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return result, nil
}

// SplitOnEmptyLine splits a slice of strings into groups based on empty lines
func SplitOnEmptyLine(lines []string) [][]string {
	var groups [][]string
	var currentGroup []string
	for _, line := range lines {
		if strings.TrimSpace(line) == "" {
			if len(currentGroup) > 0 {
				groups = append(groups, currentGroup)
				currentGroup = nil
			}
		} else {
			currentGroup = append(currentGroup, line)
		}
	}
	if len(currentGroup) > 0 {
		groups = append(groups, currentGroup)
	}
	return groups
}

func Timeit(name string) func() {
	start := time.Now()

	return func() {
		duration := time.Since(start)
		fmt.Printf("%s took %s", name, duration)
	}
}
