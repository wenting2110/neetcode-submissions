class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        maxlength, idx,tmp = 1, 0, 1
        nums.sort()


        while idx < (len(nums) -1): 
            
            if nums[idx + 1] == nums[idx]:
                idx += 1
                continue

            elif nums[idx + 1] == nums[idx] + 1:
                tmp += 1
                idx += 1
            else:
                maxlength = max(maxlength, tmp)
                tmp = 1
                idx += 1
            maxlength = max(maxlength, tmp)

        return maxlength