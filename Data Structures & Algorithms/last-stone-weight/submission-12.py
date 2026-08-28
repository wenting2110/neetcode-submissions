# Bucket Sort: O(n + w), where w is the max value in the stones
# Instead of tracking every stone individually, we store how many stones exist for each possible weight.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1) # store # of weight
        for stone in stones:
            bucket[stone] += 1

        first = second = maxStone
        while first > 0:

            if bucket[first] % 2 == 0:
                '''
                If the count at this weight is even, 
                all stones cancel in pairs.
                '''
                first -= 1
                continue
            
            # If odd, one stone remains; 
            # find the next heaviest stone to smash with it.
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            if j == 0:
                return first
            
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first