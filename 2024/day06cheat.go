package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// turnRight rotates a direction vector 90° clockwise.
// For a direction (dr, dc), the new direction is (dc, -dr).
func turnRight(dr, dc int) (int, int) {
	return dc, -dr
}

func main() {
	// Open the input file.
	file, err := os.Open("day06.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// Read the file line by line into a 2D slice of runes.
	var grid [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// Trim any potential trailing newline spaces.
		line := strings.TrimRight(scanner.Text(), "\n")
		grid = append(grid, []rune(line))
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}

	// Find the starting position (the cell that contains '^') and set the initial direction.
	var startRow, startCol int
	found := false
	// Default initial direction for '^' is "up": (-1, 0).
	var dr, dc int = -1, 0

	for i, row := range grid {
		for j, cell := range row {
			if cell == '^' {
				startRow, startCol = i, j
				found = true
				break
			}
		}
		if found {
			break
		}
	}
	if !found {
		panic("no starting position '^' found in the input file")
	}

	// Use a map to record visited positions.
	// The key is a string "row,col".
	visited := make(map[string]bool)
	visit := func(r, c int) {
		key := fmt.Sprintf("%d,%d", r, c)
		visited[key] = true
	}

	// Mark the starting cell as visited.
	currRow, currCol := startRow, startCol
	visit(currRow, currCol)

	// Simulate the guard's movement.
	// The guard continues until the next move would leave the maze.
	for {
		// Compute the next coordinates based on the current direction.
		nextRow := currRow + dr
		nextCol := currCol + dc

		// Check if the next position is out of bounds.
		if nextRow < 0 || nextRow >= len(grid) || nextCol < 0 || nextCol >= len(grid[0]) {
			// The guard leaves the maze.
			break
		}

		// If there is an obstacle directly in front, turn right.
		if grid[nextRow][nextCol] == '#' {
			dr, dc = turnRight(dr, dc)
			// Do not move this turn; try the new direction on the next iteration.
			continue
		}

		// Otherwise, move forward into the open cell.
		currRow, currCol = nextRow, nextCol
		visit(currRow, currCol)
		fmt.Println(currRow, currCol)
	}

	// Output the number of distinct visited positions.
	fmt.Println("Visited distinct positions:", len(visited))
}
