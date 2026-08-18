class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        arr = sorted(nums) # [-4, -1, -1, 0, 1, 2]
        for i in range(len(arr)-2):
            j = len(arr) - 1
            while i < j - 1:
                temp = -(arr[i] + arr[j])
                
                if temp in arr[i+1 : j]:
                    res.add(tuple([arr[i], temp, arr[j]]))
                # 每次 j 都往左縮一步，確保固定 i 的情況下，所有外側的 j 都被考慮到
                j -= 1
        return [list(t) for t in res]