class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        topK = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        sorted_by_val = sorted(freq.items(), key=lambda x: x[1]) # item = (key, val)
        while k > 0:
            topK.append(sorted_by_val[-k][0])
            k -= 1
        return topK