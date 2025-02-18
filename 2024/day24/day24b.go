package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/yodigi7/advent-of-code/utils"
)

type Equation struct {
	operator, operand1, operand2, result string
}

func parseInitialCond(input string) (string, bool) {
	r := regexp.MustCompile("([xy][0-9]{2}): ([01])")
	match := r.FindStringSubmatch(input)
	var boolVal bool
	if match[2] == "0" {
		boolVal = false
	} else {
		boolVal = true
	}
	return match[1], boolVal
}

func parseEquation(input string) Equation {
	r := regexp.MustCompile("([a-z0-9]{3}) (AND|XOR|OR) ([a-z0-9]{3}) -> ([a-z0-9]{3})")
	match := r.FindStringSubmatch(input)
	return Equation{match[2], match[1], match[3], match[4]}
}

func parse(input []string) (map[string]bool, []Equation) {
	isReadingInit := true
	initCond := make(map[string]bool)
	var equations []Equation
	for _, row := range input {
		if isReadingInit {
			if len(row) == 0 {
				isReadingInit = false
				continue
			}
			key, val := parseInitialCond(row)
			initCond[key] = val
		} else {
			equations = append(equations, parseEquation(row))
		}
	}
	return initCond, equations
}

func getFn(operator string) func(bool, bool) bool {
	if operator == "AND" {
		return func(op1 bool, op2 bool) bool {
			return op1 && op2
		}
	} else if operator == "OR" {
		return func(op1 bool, op2 bool) bool {
			return op1 || op2
		}
	} else if operator == "XOR" {
		return func(op1 bool, op2 bool) bool {
			return op1 != op2
		}
	}
	panic("OOPS, uncaught operator")
}

func swap(eqs []Equation) []Equation {
	return eqs
}

func toStr(prefix string, vals map[string]bool) string {
	var solutionBuilder strings.Builder
	// Do in reverse order since
	for i := 45; i >= 0; i-- {
		var key strings.Builder
		key.WriteString(prefix)
		if i < 10 {
			// Append 0
			key.WriteString("0")
		}
		key.WriteString(strconv.Itoa(i))
		val, ok := vals[key.String()]
		if ok {
			if val {
				solutionBuilder.WriteString("1")
			} else {
				solutionBuilder.WriteString("0")
			}
		}
	}
	return solutionBuilder.String()
}

func toInt(str string) int {
	res, _ := strconv.ParseInt(str, 2, 64)
	return int(res)
}

func toBin(i int) string {
	return strconv.FormatInt(int64(i), 2)
}

func getExpectedZ(vals map[string]bool) int {
	return toInt(toStr("x", vals)) + toInt(toStr("y", vals))
}

func calcZ(vals map[string]bool) int {
	return toInt(toStr("z", vals))
}

func solve(vals map[string]bool, equations []Equation) int {
	isDefinedOperands := func(eq Equation) bool {
		_, ok1 := vals[eq.operand1]
		_, ok2 := vals[eq.operand2]
		return ok1 && ok2
	}

	updateVals := func(eq Equation) {
		vals[eq.result] = getFn(eq.operator)(vals[eq.operand1], vals[eq.operand2])
	}

	for {
		var remainingEqs []Equation
		if len(equations) == 0 {
			break
		}
		for _, eq := range equations {
			if isDefinedOperands(eq) {
				updateVals(eq)
			} else {
				remainingEqs = append(remainingEqs, eq)
			}
		}
		equations = remainingEqs
	}
	return calcZ(vals)
}

// Returns whether the equation is currently touching an important node (z08, z19, z20...)
// or somewhere down the line
func getImportantEquations(eqs []Equation) []Equation {
	var importantEqs []Equation
	// Change this to be the important bits from your input
	isImportant := map[string]bool{
		"z38": true,
		"z27": true,
		"z26": true,
		"z25": true,
		"z24": true,
		"z13": true,
		"z12": true,
		"z11": true,
	}
	added := true
	firstAdd := true
	for added {
		added = false
		for _, eq := range eqs {
			resImp, okRes := isImportant[eq.result]
			if resImp && (!okRes || firstAdd) {
				importantEqs = append(importantEqs, eq)
				isImportant[eq.result] = true
				isImportant[eq.operand1] = true
				isImportant[eq.operand2] = true
				added = true
			}
		}
		firstAdd = false
	}
	return importantEqs
}

func main() {
	defer utils.Timeit("day 24")()
	input, err := utils.ReadFileLines("day24/day24.txt")
	if err != nil {
		fmt.Println(err)
	}
	vals, equations := parse(input)
	fmt.Println("Check the bits to see which positions are likely important")
	fmt.Println(toBin(getExpectedZ(vals)))
	fmt.Println(toBin(solve(vals, equations)))
	fmt.Println("The equations we most likely need to swap:", getImportantEquations(equations))
}

// Chars 7-8, 17-22, 32-35
// z46-7 = z39
// 7-8 = z39-z38
// 17-22 = z29-z24
// 32-35 = z14-z11
// Likely to just be 8, 19, 20, 21, 22, 33, 34, 35 because of carrying when adding
// only swap nodes that are touching these
// 1010110111011010010111101010000100011011100110
// 1010111011011010101000101010000011111011100110
