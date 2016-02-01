#!/usr/bin/env python2.7


'''
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
'''

class Solution(object):
    def can_attend_meetins(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if intervals is None:
            return False
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda x: x.start)
        for i in range(len(intervals) - 1):
            if self.is_overlap(intervals[i], intervals[i + 1]):
                return False

        return True

    def is_overlap(self, interval1, interval2):
        return interval2.start < interval1.end