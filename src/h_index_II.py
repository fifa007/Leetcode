#!/usr/bin/env python2.7


'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Show Hint
'''

class Solution(object):
    def hindex(self, citations):
        N = len(citations)
        left, right = 0, N-1
        while left <= right:
            mid = left + (right-left)/2
            if N-mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return N - left