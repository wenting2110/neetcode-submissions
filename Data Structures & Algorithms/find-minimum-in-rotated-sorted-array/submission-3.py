# binary search: O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]: # min 在 m or m 的左邊
                r = m
            else:   # min 在 m 右邊
                l = m + 1
        
        return nums[l]