#!/usr/bin/env python2.7

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''


class Solution(object):
    def helper(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.helper(n, m, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(k/2, m)
        p2 = n - p1
        if nums1[p1-1] < nums2[p2-1]:
            return self.helper(nums1[p1:], nums2, k-p1)
        else:
            return self.helper(nums1, nums2[p2:], k-p2)

    def find_sorted_median(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 == 0:
            return (self.helper(nums1, nums2, (m + n)/2) + self.helper(nums1, nums2, (m+n)/2 + 1)) / 2.0
        else:
            return self.helper(nums1, nums2, (m+n)/2+1)