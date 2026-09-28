"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[j].start < intervals[i].end:
                    return False
        
        return True