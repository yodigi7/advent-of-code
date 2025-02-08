package main

import (
	"fmt"

	"github.com/yodigi7/advent-of-code/utils"
)

type Position struct {
	i, j int
}

func getStartCoords(grid [][]int) []Position {
	var positions []Position
	for i, row := range grid {
		for j, val := range row {
			if val == 0 {
				positions = append(positions, Position{i, j})
			}
		}
	}
	return positions
}

func getNextPositions(pos Position) []Position {
	return []Position{{pos.i, pos.j + 1}, {pos.i, pos.j - 1}, {pos.i + 1, pos.j}, {pos.i - 1, pos.j}}
}

func main() {
	defer utils.Timeit("day 10")()
	grid, err := utils.ReadFileIntGrid("day10/day10.txt")
	if err != nil {
		fmt.Println(err)
	}
	isValidPosition := func(pos Position) bool {
		return pos.i >= 0 && pos.j >= 0 && pos.i < len(grid) && pos.j < len(grid[0])
	}

	var getTrails func(Position) int
	getTrails = func(pos Position) int {
		trails := 0
		if grid[pos.i][pos.j] == 9 {
			return 1
		}
		for _, nextPos := range getNextPositions(pos) {
			if !isValidPosition(nextPos) {
				continue
			}
			// Must be increasing by 1
			if grid[pos.i][pos.j]+1 != grid[nextPos.i][nextPos.j] {
				continue
			}
			trails += getTrails(nextPos)
		}
		return trails
	}
	getScore := func(startCoord Position) int {
		return getTrails(startCoord)
	}

	startCoords := getStartCoords(grid)
	count := 0
	for _, c := range startCoords {
		count += getScore(c)

	}
	fmt.Println(count)

}
