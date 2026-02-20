#第一个解法:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


#第二个解法:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i , num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []
#这道题难点在哪里?
"""这道题目不难,而是要想到怎样更快地找到目标值."""

#我用了什么思路?
"""第一个解法我用了暴力解法就是两个for循环,第二个解法我用了哈希表 + 一次遍历"""

#时间复杂度是多少?
"""第一个解法：时间复杂度 O(n^2)，空间复杂度 O(1)
第二个解法：时间复杂度平均 O(n)（字典查找平均 O(1)
空间复杂度 O(n)（字典最坏存下所有元素）"""