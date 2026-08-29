# dp (space optimized): space: O(1)
# reuse the input array
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):  # n-3 ~ 0
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])