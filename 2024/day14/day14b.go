package main

import (
	"fmt"
	"regexp"
	"strconv"
	"time"

	"github.com/yodigi7/advent-of-code/utils"
)

type Bot struct {
	posX, posY, velX, velY int
}

func atoi(str string) int {
	i, _ := strconv.Atoi(str)
	return i
}

func parse(input string) Bot {
	r := regexp.MustCompile("p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
	vals := r.FindStringSubmatch(input)
	posX, posY, velX, velY := atoi(vals[1]), atoi(vals[2]), atoi(vals[3]), atoi(vals[4])
	return Bot{posX, posY, velX, velY}
}

func hasGroup(res [][]int) bool {
	for i := 0; i < len(res)-3; i++ {
		for j := 0; j < len(res[0])-3; j++ {
			if res[i][j] != 0 && res[i+1][j] != 0 && res[i+2][j] != 0 && res[i][j+1] != 0 && res[i+1][j+1] != 0 && res[i+2][j+1] != 0 && res[i][j+2] != 0 && res[i+1][j+2] != 0 && res[i+2][j+2] != 0 {
				return true
			}
		}
	}
	return false
}

func getMap(bots []Bot) [][]int {
	res := make([][]int, 103)
	for i := range res {
		res[i] = make([]int, 103)
	}

	for _, bot := range bots {
		res[bot.posX][bot.posY] += 1
	}
	return res
}

func printMap(res [][]int) {
	fmt.Println("new tree")
	for _, line := range res {
		for _, val := range line {
			if val == 0 {
				fmt.Print(" ")
			} else {
				fmt.Print(val)
			}
		}
		fmt.Print("\r\n")
	}
}

func main() {
	defer utils.Timeit("day 11")()
	maxH, maxW := 103, 101
	// maxH, maxW := 7, 11
	input, err := utils.ReadFileLines("day14/day14.txt")
	if err != nil {
		fmt.Println(err)
	}

	move := func(bot Bot) (int, int) {
		posX, posY, velX, velY := bot.posX, bot.posY, bot.velX, bot.velY
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

	var bots []Bot
	for _, row := range input {
		bots = append(bots, parse(row))
	}
	// Adjust the max until you find it
	for i := 0; i < 10000; i += 1 {
		for j := range bots {
			bots[j].posX, bots[j].posY = move(bots[j])
		}
		botMap := getMap(bots)
		// If there is a group of 3x3 of bots then print as it likely is the tree
		if hasGroup(botMap) {
			fmt.Println(i + 1)
			printMap(botMap)
			time.Sleep(1 * time.Second)
		}
	}
}
