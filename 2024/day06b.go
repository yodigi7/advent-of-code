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
	return nil, errors.New("Unable to find start coords, likely overidden with #")
}

func genOutOfBounds(maze [][]string) func([]int) bool {
	return func(coord []int) bool {
		return coord[0] >= len(maze) || coord[1] >= len(maze[0]) || coord[0] < 0 || coord[1] < 0
	}
}

func getVisitedCoords(maze [][]string) map[int]map[int]bool {
	isOutOfBounds := genOutOfBounds(maze)
	isWall := genIsWall(maze)

	currCoord, _ := findStartCoords(maze)
	visited := make(map[int]map[int]bool)
	move := []int{-1, 0}
	markVisited := func(coord []int) {
		if _, ok := visited[coord[0]]; !ok {
			visited[coord[0]] = make(map[int]bool)
		}
		visited[coord[0]][coord[1]] = true
	}
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

func isLoop(maze [][]string) bool {
	isOutOfBounds := genOutOfBounds(maze)
	isWall := genIsWall(maze)

	currCoord, err := findStartCoords(maze)
	if err != nil {
		// Invalid so cannot count as loop
		return false
	}
	visited := make(map[Position]bool)
	move := []int{-1, 0}
	markVisited := func(coord []int, move []int) {
		visited[Position{coord[0], coord[1], move[0], move[1]}] = true
	}
	isVisited := func(coord []int, move []int) bool {
		_, ok := visited[Position{coord[0], coord[1], move[0], move[1]}]
		return ok
	}
	for true {
		nextCoords := getNextCoord(currCoord, move)
		// get next coords
		if isVisited(nextCoords, move) {
			return true
		}
		if isOutOfBounds(nextCoords) {
			return false
		}
		if !isWall(nextCoords) {
			currCoord = nextCoords
			markVisited(currCoord, move)
			continue
		}
		move = turn(move)
	}
	panic("impossible")
}

func placeBarrel(maze [][]string, i int, j int) [][]string {
	newMaze := make([][]string, len(maze))
	for i, row := range maze {
		newMaze[i] = make([]string, len(row))
		copy(newMaze[i], row)
	}
	newMaze[i][j] = "#"
	return newMaze
}

func main() {
	defer utils.Timeit("Day 6 B")()
	maze, err := utils.ReadFileCharByChar("day06.txt")
	if err != nil {
		fmt.Println(err)
	}

	visited := getVisitedCoords(maze)

	count := 0
	for i, v := range visited {
		for j := range v {
			newMaze := placeBarrel(maze, i, j)
			if isLoop(newMaze) {
				count += 1
			}
		}
	}
	fmt.Println(count)
}
