class Solution:
    def findAnagrams(self, s: str, p: str ) -> list[int]:
        s_len, p_len = len(s) , len(p)

        if s_len < p_len:
            return []
        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        
        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)
        
        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1 
            elif count[ord(s[i]) - 97] == 0:
                differ += 1
            count[ord(s[i]) - 97] -= 1
    
            if count[ord(s[i + p_len]) - 97] == -1:
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                ans.append(i + 1 )

        return ans
    
s = Solution()
print(s.findAnagrams("shaduiahsiduha","hs"))


#时间复杂度是多少?
"""时间复杂度 O(n)，其中 n 是字符串 s 的长度。空间复杂度 O(1)，因为 count 数组的大小是固定的 26。"""

#我用了什么思路?
"""滑动窗口 + 计数数组：使用一个长度为 26 的数组来记录当前窗口中每个字符的出现次数，通过比较窗口内字符的计数与目标字符串 p 的计数来判断是否为 anagram。"""

#这道题难点在哪里?
"""需要高效地判断当前窗口内的字符是否与目标字符串 p 的字符组成 anagram，使用计数数组和一个 differ 变量来跟踪不同字符的数量，可以在 O(1) 时间内更新和判断。"""