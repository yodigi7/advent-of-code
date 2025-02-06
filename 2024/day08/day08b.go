package main

import (
	"fmt"

	"github.com/yodigi7/advent-of-code/utils"
)

type Position struct {
	i, j int
}

func getFrequencies(grid [][]string) []string {
	var frequencies []string
	checkedFrequencies := make(map[string]bool)
	checkedFrequencies["."] = true
	for _, row := range grid {
		for _, val := range row {
			if _, ok := checkedFrequencies[val]; !ok {
				checkedFrequencies[val] = true
				frequencies = append(frequencies, val)
			}
		}
	}
	return frequencies
}

// Just extend line out 50 since that is the length of the grid in all directions.
// Most likely will overshoot but doesn't matter since it still runs very fast
func getAllAntinodes(pos1 Position, pos2 Position) []Position {
	deltaI := pos1.i - pos2.i
	deltaJ := pos1.j - pos2.j
	var positions []Position
	for i := 0; i < 50; i++ {
		positions = append(positions, []Position{{pos1.i + i*deltaI, pos1.j + i*deltaJ}, {pos2.i - i*deltaI, pos2.j - i*deltaJ}}...)
	}
	return positions
}

func getAntinodes(coords []Position) []Position {
	var positions []Position
	for i := 0; i < len(coords)-1; i++ {
		for j := i + 1; j < len(coords); j++ {
			pos1 := coords[i]
			pos2 := coords[j]
			positions = append(positions, getAllAntinodes(pos1, pos2)...)
		}
	}
	return positions
}

func main() {
	defer utils.Timeit("day 8")()
	grid, err := utils.ReadFileCharByChar("day08/day08.txt")
	if err != nil {
		fmt.Println(err)
	}
	getCoords := func(freq string) []Position {
		var coords []Position
		for i, row := range grid {
			for j, val := range row {
				if val == freq {
					coords = append(coords, Position{i, j})
				}
			}
		}
		return coords
	}
	onGrid := func(pos Position) bool {
		return pos.i >= 0 && pos.j >= 0 && pos.i < len(grid) && pos.j < len(grid[0])
	}

	antinodes := make(map[Position]bool)
	for _, freq := range getFrequencies((grid)) {
		coords := getCoords(freq)
		for _, pos := range getAntinodes(coords) {
			if onGrid(pos) {
				antinodes[pos] = true
			}
		}
	}
	count := 0
	for range antinodes {
		count += 1
	}
	fmt.Println(count)
}
