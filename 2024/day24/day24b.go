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

func main() {
	defer utils.Timeit("day 24")()
	input, err := utils.ReadFileLines("day24/day24.txt")
	if err != nil {
		fmt.Println(err)
	}
	vals, equations := parse(input)
	fmt.Println(toBin(getExpectedZ(vals)))
	fmt.Println(toBin(solve(vals, equations)))
}
