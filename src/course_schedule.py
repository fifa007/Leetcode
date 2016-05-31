#!/usr/bin/env python2.7

'''

'''


class Solution(object):
    def schedule_course(self, n, pairs):
        if n == 0 or pairs is None or len(pairs) == 0:
            return False
        preq = [[] for i in xrange(n)]
        cnts = [0] * n
        for p in pairs:
            preq[p[1]].append(p[0])
            cnts[p[0]] += 1

        q = []
        for i in xrange(n):
            if cnts[i] == 0:
                q.append(p[0])

        while q:
            tmp = q.pop(0)
            for j in preq[tmp]:
                cnts[j] -= 1
                if cnts[j] == 0:
                    q.append(j)

        for i in xrange(n):
            if cnts[i] != 0:
                return False
        return True