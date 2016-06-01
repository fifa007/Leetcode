#!/usr/bin/env python2.7

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def next_permutations(self, nums):
        if nums is None or len(nums) == 0:
            return
        n = len(nums)
        j = n - 1
        while j > 0:
            if nums[j-1] < nums[j]:
                break
            j -= 1
        if j > 0:
            j -= 1
            right = n - 1
            while right > 0:
                if nums[right] > nums[j]:
                    break
                right -= 1
            nums[j], nums[right] = nums[right], nums[j]
            j += 1
        end = n - 1
        while j < end:
            nums[j], nums[end] = nums[end], nums[j]
            j += 1
            end -= 1
        return