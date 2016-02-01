#!/usr/bin/env python2.7


'''
unit test for meeting rooms
'''


import unittest
import src.data_structure
import src.meeting_rooms


class meeting_rooms_test(unittest.TestCase):
    sol = src.meeting_rooms.Solution()

    def test_with_null_intervals(self):
        self.failUnless(self.sol.can_attend_meetins(None) == False)

    def test_with_one_meeting(self):
        intervals = [src.data_structure.Interval(0, 30)]
        self.failUnless(self.sol.can_attend_meetins(intervals) == True)

    def test_with_overlapped_meetings(self):
        interval1 = src.data_structure.Interval(0, 30)
        interval2 = src.data_structure.Interval(5, 10)
        interval3 = src.data_structure.Interval(15, 20)
        intervals = [interval1, interval2, interval3]
        self.failUnless(self.sol.can_attend_meetins(intervals) == False)

    def test_with_no_overlap(self):
        interval1 = src.data_structure.Interval(0, 5)
        interval2 = src.data_structure.Interval(5, 10)
        interval3 = src.data_structure.Interval(15, 20)
        intervals = [interval1, interval2, interval3]
        self.failUnless(self.sol.can_attend_meetins(intervals) == True)