class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)-1, i, -1):
                profit = max(profit, prices[j] - prices[i])

        return profit
