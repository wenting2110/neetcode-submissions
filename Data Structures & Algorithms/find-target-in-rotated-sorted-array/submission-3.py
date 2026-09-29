class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # pivot 在 m 右邊
                l = m + 1
            else:
                # pivot 在 m (含)左邊
                r = m
        
        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            # target 在 pivot 右半邊(含)
            l = pivot
        else:
            # target 在 pivot 左邊
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        