#!/usr/bin/env python2.7

'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def remove_dupe(self, nums):
        if nums is None:
            return 0
        n = len(nums)
        if n <= 2:
            return n
        i = 0
        j = i + 1
        c = 1
        while j < n:
            while j < n and nums[j] == nums[i]:
                c += 1
                if c == 2:
                    nums[i+1] = nums[j]
                    i += 1
                j += 1
            if j == n:
                break
            nums[i+1], nums[j] = nums[j], nums[i+1]
            i += 1
            j += 1
            c = 1
        return i + 1