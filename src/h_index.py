#!/usr/bin/env python2.7

'''
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h
of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total
and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3
papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''


class Solution(object):
    def h_index_1(self, citations):
        N = len(citations)
        cnts = [0]*(N + 1)
        for c in citations:
            c[[c, N][c > N]] += 1
        sum = 0
        for h in xrange(N, 0, -1):
            if sum + cnts[h] >= h:
                return h
            sum += cnts[h]
        return 0

    def h_index_2(self, citations):
        return sum(i < c for i, c in enumerate(sorted(citations, reverse=True)))