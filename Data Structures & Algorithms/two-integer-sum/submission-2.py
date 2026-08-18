# sorting O(nlogn)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for index, num in enumerate(nums):
            A.append([num, index])
        
        A.sort()
        i, j = 0, len(nums)-1
        while i < j:
            test = A[i][0] + A[j][0]
            if test == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif test < target:
                i +=1
            else:
                j -=1