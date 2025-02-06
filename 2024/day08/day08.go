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

func getBothAntinodes(pos1 Position, pos2 Position) []Position {
	deltaI := pos1.i - pos2.i
	deltaJ := pos1.j - pos2.j
	return []Position{{pos1.i + deltaI, pos1.j + deltaJ}, {pos2.i - deltaI, pos2.j - deltaJ}}
}

func getAntinodes(coords []Position) []Position {
	var positions []Position
	for i := 0; i < len(coords)-1; i++ {
		for j := i + 1; j < len(coords); j++ {
			pos1 := coords[i]
			pos2 := coords[j]
			positions = append(positions, getBothAntinodes(pos1, pos2)...)
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
