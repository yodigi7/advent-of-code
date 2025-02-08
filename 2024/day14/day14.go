package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/yodigi7/advent-of-code/utils"
)

func atoi(str string) int {
	i, _ := strconv.Atoi(str)
	return i
}

func parse(input string) (int, int, int, int) {
	r := regexp.MustCompile("p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
	vals := r.FindStringSubmatch(input)
	posX, posY, velX, velY := atoi(vals[1]), atoi(vals[2]), atoi(vals[3]), atoi(vals[4])
	return posX, posY, velX, velY
}

func main() {
	defer utils.Timeit("day 14")()
	maxH, maxW := 103, 101
	// maxH, maxW := 7, 11
	input, err := utils.ReadFileLines("day14/day14.txt")
	if err != nil {
		fmt.Println(err)
	}

	move := func(posX int, posY int, velX int, velY int) (int, int) {
		posX = posX + velX
		posY = posY + velY
		if posX >= maxW {
			posX -= maxW
		} else if posX < 0 {
			posX += maxW
		}
		if posY >= maxH {
			posY -= maxH
		} else if posY < 0 {
			posY += maxH
		}
		return posX, posY
	}
	solve := func(posX int, posY int, velX int, velY int) int {
		for i := 0; i < 100; i++ {
			posX, posY = move(posX, posY, velX, velY)
		}
		if posX == maxW/2 || posY == maxH/2 {
			return 0
		}
		if posX < maxW/2 {
			if posY < maxH/2 {
				return 1
			} else {
				return 3
			}
		} else {
			if posY < maxH/2 {
				return 2
			} else {
				return 4
			}
		}
	}
	counts := make(map[int]int)
	counts[1] = 0
	counts[2] = 0
	counts[3] = 0
	counts[4] = 0
	for _, row := range input {
		res := solve(parse(row))
		if res == 0 {
			continue
		}
		counts[res] += 1
	}
	fmt.Println(counts[1] * counts[2] * counts[3] * counts[4])
}
