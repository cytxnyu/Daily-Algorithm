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