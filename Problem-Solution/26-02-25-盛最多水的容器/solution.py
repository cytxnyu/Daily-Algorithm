class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

#时间复杂度是多少?
"""时间复杂度 O(n)，空间复杂度 O(1)"""

#我用了什么思路?
"""双指针：一个指针 l 从左向右移动，另一个指针 r 从右向左移动。每次计算当前面积并更新最大值，然后移动较短的指针，因为移动较长的指针不可能得到更大的面积。"""

#这道题难点在哪里?
"""需要找到一种方法在 O(n) 时间内计算所有可能的容器面积，双指针方法可以高效地实现这一点。"""