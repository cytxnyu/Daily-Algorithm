from typing import List 
class Solution:
    def rotate(self , nums: List[int], k : int ) -> List[int]:
        def reverse(i : int , j : int ) -> List[int]:
            while i < j:
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        n = len(nums)
        k %= n
        reverse(0 , n -1 )
        reverse(0 , k -1 )
        reverse(k , n - 1)
        return nums

s = Solution()
nums = [1,2,3,4,5,6,7]
print(s.rotate(nums, 3))
#输入: nums = [1,2,3,4,5,6,7], k = 3
#输出: [5,6,7,1,2,3,4]
