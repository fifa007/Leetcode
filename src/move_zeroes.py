#!/usr/bin/python2.7


'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

__author__ = 'hao.chen'

class Solution(object):
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return
        p1 = 0
        p2 = 0
        for num in nums:
            if num == 0:
                break
            p1 += 1
            p2 += 1

        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.move_zeroes(nums)
    print nums
