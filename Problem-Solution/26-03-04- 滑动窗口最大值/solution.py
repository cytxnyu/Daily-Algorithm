import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans

#时间复杂度是多少?
"""时间复杂度 O(n log k)，其中 n 是数组 nums 的长度，k 是窗口的大小。空间复杂度 O(k)，因为优先队列中最多存储 k 个元素。"""

#我用了什么思路?
"""优先队列（堆）：使用一个最大堆来维护当前窗口中的元素，堆顶元素即为当前窗口的最大值。每次移动窗口时，将新元素加入堆，并移除过期的元素。"""

#这道题难点在哪里?
"""需要高效地维护当前窗口中的最大值，使用优先队列可以在 O(log k) 时间内更新和获取最大值，同时需要注意移除过期元素。"""
