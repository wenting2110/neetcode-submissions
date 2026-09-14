# O(n) is trivial
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1::]:
            res = num if num < res else res
        
        return res