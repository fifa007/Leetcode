#!/usr/bin/env python2.7

'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
import heapq


class Solution(object):
    def find_kth_largest(self, nums, k):
        h = []
        i = 0
        n = len(nums)
        while i < k:
            h.append(nums[i])
            i += 1
        heapq.heapify(h)
        while i < n:
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, nums[i])
            i += 1
        return h[0]k