package main

import (
	"fmt"

	"github.com/yodigi7/advent-of-code/utils"
)

var powers = []int64{1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000}

func Pow10(e int) int64 {
	return powers[e]
}

func splitInteger(num int64) (left, right int64, digits int) {
	temp := num
	for temp > 0 {
		digits++
		temp /= 10
	}
	divisor := int64(Pow10(digits / 2))
	left = num / divisor
	right = num % divisor
	return
}

func genUpdateStone() func(int64) []int64 {
	cache := make(map[int64][]int64)

	return func(stone int64) []int64 {
		if stone == 0 {
			return []int64{1}
		} else if source, ok := cache[stone]; ok {
			destinationSlice := make([]int64, len(source))
			copy(destinationSlice, source)
			return destinationSlice
		} else if l, r, digits := splitInteger(stone); digits%2 == 0 {
			return []int64{l, r}
		} else {
			cache[stone] = []int64{stone * 2024}
			return []int64{stone * 2024}
		}
	}

}

func main() {
	defer utils.Timeit("day 11")()
	input, err := utils.ReadFileListOfInts("day11/day11.txt")
	if err != nil {
		fmt.Println(err)
	}
	updateStone := genUpdateStone()
	stones := make(map[int64]int64)
	for _, stone := range input[0] {
		if _, ok := stones[int64(stone)]; !ok {
			stones[int64(stone)] = 0
		}
		stones[int64(stone)] += 1
	}
	fmt.Println(stones)
	for i := 0; i < 75; i++ {
		// for i := 0; i < 25; i++ {
		// fmt.Println(stones)
		fmt.Println("iteration", i)
		// fmt.Println("len", len(stones))
		newStones := make(map[int64]int64)
		for stone, count := range stones {
			updatedStones := updateStone(stone)
			for _, updatedStone := range updatedStones {
				if _, ok := newStones[int64(updatedStone)]; !ok {
					newStones[int64(updatedStone)] = 0
				}
				newStones[int64(updatedStone)] += count
				// fmt.Println("stone", stone)
				// fmt.Println("stones[stone]", stones[stone])
				// fmt.Println("count", count)
			}
		}
		stones = newStones
	}

	count := int64(0)
	for _, val := range stones {
		count += val
	}
	fmt.Println(count)
}
