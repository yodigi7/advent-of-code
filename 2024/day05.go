package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func readFile() (map[string][]string, [][]string) {
	file, err := os.Open("day05.txt") // Replace with your file name
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, nil
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	rules := make(map[string][]string)
	var updates [][]string
	for scanner.Scan() {
		line := scanner.Text()

		// Stop reading when an empty line is encountered
		if strings.TrimSpace(line) == "" {
			break
		}

		split := strings.Split(line, "|")
		rules[split[0]] = append(rules[split[0]], split[1])
	}

	for scanner.Scan() {
		line := scanner.Text()

		split := strings.Split(line, ",")
		updates = append(updates, split)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
	return rules, updates
}

func inCorrectOrder(rules map[string][]string, update []string) bool {
	invalid := false
	var seen []string
	for _, page := range update {
		if invalid {
			break
		}
		for _, rule := range rules[page] {
			if slices.Contains(seen, rule) {
				return false
			}
		}
		seen = append(seen, page)
	}
	return true
}

func generateIsValidPage(rules map[string][]string) func([]string, string) bool {
	return func(pagesLeft []string, page string) bool {
		for _, pageCheck := range pagesLeft {
			if page == pageCheck {
				continue
			}
			if slices.Contains(rules[page], pageCheck) {
				return false
			}
		}
		return true
	}
}

func remove(slice []string, item string) []string {
	// remove from pagesLeft
	index := slices.Index(slice, item)
	if index == -1 {
		panic("THIS SHOULDN'T HAPPEN")
	}
	return append(slice[:index], slice[index+1:]...)
}

func generateOrder(rules map[string][]string) func([]string) []string {
	isValidPage := generateIsValidPage(rules)
	return func(update []string) []string {
		var res []string
		pagesLeft := make([]string, len(update))
		copy(pagesLeft, update)
		for true {
			if len(pagesLeft) == 1 {
				res = append(res, pagesLeft[0])
				break
			}
			var pageToRemove string
			for _, page := range pagesLeft {
				if isValidPage(pagesLeft, page) {
					res = append(res, page)
					pageToRemove = page
					break
				}
			}
			pagesLeft = remove(pagesLeft, pageToRemove)
		}
		slices.Reverse(res)
		fmt.Println(res)
		return res
	}
}

func getMiddlePageNum(update []string) (int, error) {
	if len(update)%2 == 0 {
		fmt.Println(update)
		panic("OH NO, THIS SHOULDN'T HAPPEN")
	}
	return strconv.Atoi(update[len(update)/2])
}

func main() {
	rules, updates := readFile()
	sum := 0
	order := generateOrder(rules)
	for _, update := range updates {
		if inCorrectOrder(rules, update) {
			// res, _ := getMiddlePageNum(update)
			// sum += res
		} else {
			res, _ := getMiddlePageNum(order(update))
			sum += res
		}
	}
	fmt.Println(sum)
}
