# dp: O(n)
# Let dp[i] represent the minimum cost to reach step i.
# 比較直覺，但跟我想的 sol_1 有些不同
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # 0 ~ n

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]
            