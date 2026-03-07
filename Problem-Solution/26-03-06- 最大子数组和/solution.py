class Solution:
    def maxSubArray(self, nums: list[int]) ->int:
        cur = 0
        res = nums[0]
        for x in nums:
            cur = max(x , cur + x)
            res = max(res, cur)
        return res        