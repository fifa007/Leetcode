#!/usr/bin/env python2.7

'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
'''

class Solution(object):
    def find_intersection(self, A, B, C, D, E, F, G, H):
        if G < A or E > C or H < B or F > D:
            return 0
        bottom_left_x = max(A, E)
        bottom_left_y = max(B, F)
        top_right_x = min(C, G)
        top_right_y = min(D, H)
        return abs(bottom_left_x - top_right_x) * abs(bottom_left_y - top_right_y)

    def compute_area(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = abs(A-C)*abs(B-D)
        area2 = abs(E-G)*abs(F-H)
        intersection = self.find_intersection(A, B, C, D, E, F, G, H)
        return area1 + area2 - intersection
