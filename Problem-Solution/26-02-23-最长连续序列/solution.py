class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak



#时间复杂度是多少?
"""平均/期望 O(n)（建 HashSet 一次 + 每个数最多被“向右扩展”访问一次）；空间复杂度 O(n)。
（如果用排序做：时间 O(n log n)，空间看排序实现。）"""
#我用了什么思路?
"""把所有数放进集合；遍历每个数 x，若 x-1 不在集合里，说明 x 是一段连续序列的起
点，然后不断检查 x+1, x+2, ... 是否在集合中来得到长度并更新答案。"""
#这道题难点在哪里?
"""怎么做到 O(n)：避免对每个数都往两边/往右重复扫描；关键是“只从起点扫描”，否则会退化成重复工作。
处理重复元素：数组里可能有重复值，用集合天然去重，但遍历逻辑要不受重复影响。
边界与数值范围：负数、很大的数都要支持；不能用按值开数组的思路。"""