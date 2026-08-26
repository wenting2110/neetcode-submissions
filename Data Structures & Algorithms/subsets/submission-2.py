# bit manulation: O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        i (外層迴圈)：代表一種「選取組合」。
        它是一個數字，其二進位（例如 101) 直接決定了這一次要選第 0 個和第 2 個元素。

        j (內層迴圈)：負責逐一檢查 nums[j] 是否放進當前的 subset。

        i 給出開關藍圖，
        j 負責按藍圖把元素放入集合。
        '''
        n = len(nums)
        res = []
        for i in range(1 << n): # i = 0 ~ (2^n -1)
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            res.append(subset)

        return res