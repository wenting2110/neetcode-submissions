# sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, tmp = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                tmp = 0
            
            while i < len(nums) and nums[i] == curr: 
                # 重複數字 -> 跳過
                i += 1
            
            tmp += 1
            curr += 1
            res = max(res, tmp)
        
        return res