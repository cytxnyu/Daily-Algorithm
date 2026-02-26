class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            target = -nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second],nums[third]])
        return ans
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))


#时间复杂度是多少?
"""时间复杂度 O(n^2)，空间复杂度 O(1)（不考虑输出空间）"""

#我用了什么思路?
"""排序 + 双指针：首先对数组进行排序，然后固定一个元素，使用双指针在剩余部分寻找两个数，使得三数之和为零。通过跳过重复元素来避免重复解。"""

#这道题难点在哪里?
"""需要找到一种方法在 O(n^2) 时间内找到所有满足条件的三元组，并且避免重复解，排序和双指针方法可以高效地实现这一点。"""