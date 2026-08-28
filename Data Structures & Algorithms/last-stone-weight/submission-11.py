# max-heap: O(nlogn)
# Most languages provide min-heaps, so a common trick is to store negative values.
# This makes the smallest (most negative) value represent the largest stone.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative and build a heap.
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)

        return abs(stones[0])