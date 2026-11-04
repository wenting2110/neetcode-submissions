# linear search
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            # i.end < new.start ([1,2], [3,5])
            res.append(intervals[i])
            i += 1

        # i.end >= new.start ([4,8], [2,3])
        while i < n and newInterval[1] >= intervals[i][0]:
            # new.end >= i.start ([4,8], [2,9])
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            # [2,9]
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

