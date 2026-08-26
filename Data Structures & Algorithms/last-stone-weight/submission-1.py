class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones[-1]
            x = stones[-2]
            stones = stones[0 : len(stones) - 2]
            if x < y:
                stones.append(y - x)
                stones.sort()
        
        return stones[0] if len(stones) == 1 else 0
                