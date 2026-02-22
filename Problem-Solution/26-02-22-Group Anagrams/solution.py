#第一种解法: 排 序:由于互为字母异位词的两个字符串包含的字母相同，因此对两个字符串分别进行排序之后得到的字符串一定是相同的，    
#                 故可以将排序之后的字符串作为哈希表的键。
import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
    
#第二种解法: 计 数:由于互为字母异位词的两个字符串包含的字母相同，因此对两个字符串分别进行计数之后得到的结果一定是相同的，

class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要讲 list 转换成 tuple 才能作为哈希表的键
            mp[tuple(counts)].append(st)
        
        return list(mp.values())
    

#这道题难点在哪里?
"""关键在于“怎么给每个字符串生成一个唯一且可哈希的分组标识（key）”，使得同一组异位词得到相同 key、不同组尽量不同 key。"""

#我用了什么思路?
"""
(1)排序作为 key
对每个字符串排序：key = "".join(sorted(st))，用 defaultdict(list) 把原串追加到 mp[key]。

(2)26 字母频次数组作为 key
统计每个字符串 26 个字母出现次数，counts 转 tuple(counts) 作为 key，再分组。"""
#时间复杂度是多少?
"""
排序法：每个串排序 O(k log k)，总时间 O(n * k log k)；额外空间（不含输出）约 O(n * k)（存 key/排序结果）。
计数法：每个串计数 O(k)，总时间 O(n * k)；额外空间约 O(n)（每个 key 是 26 维 tuple，常数级）。 """
