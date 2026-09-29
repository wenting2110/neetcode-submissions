# binary serach: O(logn)
# find the pivot — the index of the smallest element.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # Find the pivot — the index of the smallest element.
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # pivot 在 m 右邊
                l = m + 1
            else:
                # pivot 在 m 左邊
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)
        