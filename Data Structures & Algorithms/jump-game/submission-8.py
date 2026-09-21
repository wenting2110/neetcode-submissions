class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 1
        res = False

        # 法一
        # for i in range(len(nums) - 2, -1, -1):

        # 法二
        for num in nums[-2:: -1]: # [start: stop: step]
            if num < jump:
                jump += 1
                res = False
            else:
                jump = 1
                res = True

        return res if len(nums) > 1 else True