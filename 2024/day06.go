package main

import (
	"errors"
	"fmt"

	"github.com/yodigi7/advent-of-code/utils"
)

type Position struct {
	coord1, coord2, move1, move2 int
}

func genIsWall(maze [][]string) func([]int) bool {
	return func(coord []int) bool {
		return maze[coord[0]][coord[1]] == "#"
	}
}

func turn(move []int) []int {
	return []int{move[1], -move[0]}
}

func getNextCoord(curr []int, move []int) []int {
	return []int{curr[0] + move[0], curr[1] + move[1]}
}

func findStartCoords(maze [][]string) ([]int, error) {
	for i, row := range maze {
		for j, val := range row {
			if val == "^" {
				return []int{i, j}, nil
			}
		}
	}
	return nil, errors.New("Unable to find start coords, likely overidden with X")
}

func genOutOfBounds(maze [][]string) func([]int) bool {
	return func(coord []int) bool {
		return coord[0] >= len(maze) || coord[1] >= len(maze[0]) || coord[0] < 0 || coord[1] < 0
	}
}

func getVisitedCoords(maze [][]string) map[int]map[int]bool {
	isOutOfBounds := genOutOfBounds(maze)
	isWall := genIsWall(maze)

	currCoord := findStartCoords(maze)
	visited := make(map[int]map[int]bool)
	move := []int{-1, 0}
	markVisited := func(coord []int) {
		if _, ok := visited[coord[0]]; !ok {
			visited[coord[0]] = make(map[int]bool)
		}
		visited[coord[0]][coord[1]] = true
	}
	markVisited(currCoord)
	for true {
		nextCoords := getNextCoord(currCoord, move)
		// get next coords
		if isOutOfBounds(nextCoords) {
			return visited
		}
		if !isWall(nextCoords) {
			currCoord = nextCoords
			markVisited(currCoord)
			continue
		}
		move = turn(move)
	}
	panic("impossible")
}

func main() {
	defer utils.Timeit("day 6")()
	maze, err := utils.ReadFileCharByChar("day06.txt")
	if err != nil {
		fmt.Println(err)
	}

	visited := getVisitedCoords(maze)

	// fmt.Println(len(maze), len(maze[0]))
	count := 0
	for _, v := range visited {
		count += len(v)
	}
	fmt.Println(count)
}
