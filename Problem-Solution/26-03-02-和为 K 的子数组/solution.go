package main

func subarraySum(nums []int, k int) int {
	count := 0
	for start := 0; start < len(nums); start++ {
		sum := 0
		for end := start; end >= 0; end-- {
			sum += nums[end]
			if sum == k {
				count++
			}
		}
	}
	return count
}

//时间复杂度是多少?
/*时间复杂度 O(n^2)，其中 n 是数组 nums 的长度。空间复杂度 O(1)。*/

//我用了什么思路?
//暴力枚举所有子数组，计算每个子数组的和，统计和等于 k 的子数组个数。"""

//这道题难点在哪里?
//需要枚举所有可能的子数组，并计算它们的和，时间复杂度较高。"""

func subarraySum2(nums []int, k int) int {
	count, pre := 0, 0
	m := map[int]int{}
	m[0] = 1
	for i := 0; i < len(nums); i++ {
		pre += nums[i]
		if _, ok := m[pre-k]; ok {
			count += m[pre-k]
		}
		m[pre] += 1
	}
	return count
}

//时间复杂度是多少?
/*时间复杂度 O(n)，其中 n 是数组 nums 的长度。空间复杂度 O(n)，因为哈希表最多存储 n 个不同的前缀和。*/

//我用了什么思路?
//前缀和 + 哈希表：通过计算前缀和，利用哈希表快速查找是否存在某个前缀和使得当前前缀和与该前缀和的差值等于 k。"""

//这道题难点在哪里?
//需要高效地判断当前前缀和与之前某个前缀和的差值是否等于 k，使用哈希表可以将查找时间从 O(n) 降低到 O(1)。"""
