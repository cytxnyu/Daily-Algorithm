class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

#时间复杂度是多少?
"""时间复杂度 O(n)，空间复杂度 O(1)"""

#我用了什么思路?
"""双指针：一个指针 right 遍历数组，另一个指针 left 记录下一个非零元素应该放的位置。当 right 遇到非零元素时，与 left 交换并移动 left。"""

#这道题难点在哪里?
"""需要原地操作且保持非零元素的相对顺序，双指针方法可以高效地实现这一点。"""