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

	var getEndpoints func(Position) map[Position]bool
	getEndpoints = func(pos Position) map[Position]bool {
		endpoints := make(map[Position]bool)
		if grid[pos.i][pos.j] == 9 {
			endpoints[pos] = true
			return endpoints
		}
		for _, nextPos := range getNextPositions(pos) {
			if !isValidPosition(nextPos) {
				continue
			}
			if grid[pos.i][pos.j]+1 != grid[nextPos.i][nextPos.j] {
				continue
			}
			for endpoint := range getEndpoints(nextPos) {
				endpoints[endpoint] = true
			}
		}
		return endpoints
	}
	getScore := func(startCoord Position) int {
		return len(getEndpoints(startCoord))
	}

	startCoords := getStartCoords(grid)
	count := 0
	for _, c := range startCoords {
		count += getScore(c)

	}
	fmt.Println(count)

}
