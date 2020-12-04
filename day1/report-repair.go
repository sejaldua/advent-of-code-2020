package main

import (
	"fmt"
	"io"
	"os"
)

func get_input_nums() []int {
	file, err := os.Open("input.txt")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var perline int
	var nums []int

	for {
		_, err := fmt.Fscanf(file, "%d\n", &perline)
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println(err)
			os.Exit(1)
		}
		nums = append(nums, perline)
	}
	return nums
}

func puzzle1(nums []int) int {
	var ans int
	for i := 0; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			if nums[i]+nums[j] == 2020 {
				ans = nums[i] * nums[j]
				break
			}
		}
	}
	return ans
}

func puzzle2(nums []int) int {
	var ans int
	for i := 0; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			for k := j; k < len(nums); k++ {
				if nums[i]+nums[j]+nums[k] == 2020 {
					ans = nums[i] * nums[j] * nums[k]
					break
				}
			}
		}
	}
	return ans
}

func main() {
	var nums []int = get_input_nums()
	fmt.Println(puzzle1(nums))
	fmt.Println(puzzle2(nums))
}
