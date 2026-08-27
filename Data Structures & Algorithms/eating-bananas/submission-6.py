# binary search: O(n * log m)
# Where n is the length of the input array piles  
# and m is the maximum number of bananas in a pile.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)    # possible speed range

        while l <= r:
            mid = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / mid)
            if totalTime <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return k