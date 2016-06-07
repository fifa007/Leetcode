#!/usr/bin/env python2.7


'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''

import collections

class Solution(object):
    def construct_itinerary(self, tickets):
        if tickets is None or len(tickets) == 0:
            return []
        n, self.ret = len(tickets) + 1, ['JFK']
        m = collections.defaultdict(lambda: collections.OrderedDict())
        for i, j in sorted(tickets):
            m[i].setdefault(j, 0)
            m[i][j] += 1

        self.helper('JFK', n, m)
        return self.ret

    def helper(self, curr, n, m):
        if len(self.ret) == n:
            return True
        if curr in m:
            for c, cnt in m[curr].items():
                if cnt != 0:
                    m[curr][c], self.ret = m[curr][c] - 1, self.ret + [c]
                    if self.helper(c, n, m):
                        return True
                    m[curr][c], self.ret = m[curr][c] + 1, self.ret[:-1]
        return False