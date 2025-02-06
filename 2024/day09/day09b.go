package main

import (
	"fmt"
	"sort"
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

func getGaps(disk []int) map[int]int {
	ret := make(map[int]int)
	for i := 0; i < len(disk); i++ {
		if disk[i] == -1 {
			j := i
			for j < len(disk)-1 && disk[j+1] == -1 {
				j += 1
			}
			ret[i] = 1 + j - i
			i = j + 1
		}
	}
	return ret
}

func getOrderedIndexes(gaps map[int]int) []int {
	var indexes []int
	for k := range gaps {
		indexes = append(indexes, k)
	}
	sort.Ints(indexes)
	return indexes
}

func compress(disk []int) []int {
	gaps := getGaps(disk)
	gapIdxs := getOrderedIndexes(gaps)
	for j := len(disk) - 1; j >= 0; j-- {
		val := disk[j]
		if val == -1 {
			continue
		}
		// Find the beginning of the segment
		jStart := j
		for jStart > 0 && disk[jStart-1] == val {
			jStart -= 1
		}
		length := 1 + j - jStart
		// Find gap segment that is at least this long
		for _, idx := range gapIdxs {
			// for gapIdx, idx := range gapIdxs {
			if idx > jStart {
				break
			}
			if gaps[idx] >= length {
				// Insert at idx
				for i := 0; i < length; i++ {
					disk[i+idx] = val
					disk[i+jStart] = -1
				}
				// update gaps and gapIdxs to remove the newly occupied space
				gaps = getGaps(disk)
				gapIdxs = getOrderedIndexes(gaps)
				// TODO: fix this to be more efficient, still good enough redoing everything
				// gaps[idx+length] = gaps[idx] - length
				// delete(gaps, idx)
				// newIdx := idx + length
				// gapIdxs = append(gapIdxs[:gapIdx], append([]int{newIdx}, gapIdxs[gapIdx+1:]...)...)
				// if gaps[idx] == 0 {
				// 	gapIdxs = append(gapIdxs[:gapIdx], gapIdxs[gapIdx+1:]...)
				// }
				break
			}
		}
		j = jStart
	}
	return disk
}

func calcCheckSum(disk []int) int {
	checkSum := 0
	for i, val := range disk {
		if val == -1 {
			continue
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
	compressed := compress(expand(diskmap))
	fmt.Println(calcCheckSum(compressed))
}
