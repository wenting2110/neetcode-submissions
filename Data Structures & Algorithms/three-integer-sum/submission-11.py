# Hash Map: O(n^2)
# defaultdict 是 Python collections 模組中的字典子類別。
# 當你讀取不存在的鍵時，它不會跳出錯誤，而是會自動建立一個預設值。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
                
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res
            