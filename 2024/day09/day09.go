package main

import (
	"fmt"
	"strconv"

	"github.com/yodigi7/advent-of-code/utils"
)

func expand(diskmap []int) []int {
	var ret []int
	useNil := false
	num := 0
	for _, val := range diskmap {
		for i := 0; i < val; i++ {
			if useNil {
				ret = append(ret, -1)
			} else {
				ret = append(ret, num)
			}
		}
		if !useNil {
			num += 1
		}
		useNil = !useNil
	}
	return ret
}

func toIntSlice(slice []string) []int {
	intSlice := make([]int, len(slice))
	for i, strVal := range slice {
		intVal, err := strconv.Atoi(strVal)
		if err != nil {
			panic("Error converting to int")
		}
		intSlice[i] = intVal
	}
	return intSlice
}

func compress(disk []int) []int {
	j := len(disk) - 1
	for i := 0; i < len(disk) && i <= j; i++ {
		if disk[i] != -1 {
			continue
		}
		for disk[j] == -1 && j > i {
			j -= 1
		}
		disk[i] = disk[j]
		disk[j] = -1
	}
	return disk
}

func calcCheckSum(disk []int) int {
	checkSum := 0
	for i, val := range disk {
		if val == -1 {
			break
		}
		checkSum += i * val
	}
	return checkSum
}

func main() {
	defer utils.Timeit("day 9")()
	input, err := utils.ReadFileCharByChar("day09/day09.txt")
	if err != nil {
		fmt.Println(err)
	}
	diskmap := toIntSlice(input[0])
	fmt.Println(calcCheckSum(compress(expand(diskmap))))
}
