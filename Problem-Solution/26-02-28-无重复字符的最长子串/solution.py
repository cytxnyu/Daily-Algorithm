class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        occ = set()
        n = len(s)
        rk , ans = -1 , 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1 ] not in occ:
                occ.add(s[rk + 1])
                rk += 1

            ans = max(ans , rk - i + 1)
        return ans

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

#时间复杂度是多少?
"""时间复杂度 O(n)，空间复杂度 O(min(m,n))，其中 m 是字符集的大小，n 是字符串的长度。"""

#我用了什么思路?
"""滑动窗口 + 哈希表：使用一个哈希集合来维护当前窗口中的字符，通过移动右指针扩展窗口，当遇到重复字符时移动左指针缩小窗口。"""

#这道题难点在哪里?
"""需要高效地找到最长的无重复字符子串，使用滑动窗口和哈希集合可以在 O(n) 时间内实现这一点，同时需要注意处理重复字符的情况。"""