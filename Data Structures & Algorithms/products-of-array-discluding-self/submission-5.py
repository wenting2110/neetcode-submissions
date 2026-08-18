class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        flag = False

        for i in range(len(nums)):
            if nums[i] == 0:
                flag = True
                continue
            prod = prod * nums[i]
        
        for i in range(len(nums)):
            if nums.count(0) > 1:
                return [0 for x in nums]
            if flag == False:
                res.append(prod // nums[i])
            else:
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(prod)

        return res