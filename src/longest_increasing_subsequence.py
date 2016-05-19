#!/usr/bin/env python2.7


'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution1(object):
    def length_of_LIS(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        m = [1] * n
        ret = 1
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] > nums[j] and m[j] + 1 > m[i]:
                    m[i] = m[j] + 1
        for i in xrange(n):
            ret = max(ret, m[i])
        return ret

class Solution2(object):
    def find_ceiling_index(self, nums, start, end, target):
        while (end - start) > 1:
            mid = start + (end-start)/2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        return end

    def length_of_LIS(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        tail = [0] * n
        ret = 1
        for i in xrange(1, n):
            if nums[i] < tail[0]:
                tail[0] = nums[i]
            elif nums[i] > tail[ret-1]:
                tail[ret] = nums[i]
                ret += 1
            else:
                idx = self.find_ceiling_index(tail, -1, ret-1, nums[i])
                tail[idx] = nums[i]

        return ret