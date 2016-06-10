#!/usr/bin/env python2.7

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should
take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course
order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
'''


class Solution(object):
    def schedule(self, numCourses, prerequistes):
        if numCourses < 0:
            return []
        if not prerequistes or len(prerequistes) == 0:
            return [i for i in xrange(numCourses)]
        graph = [[] for i in xrange(numCourses)]
        dep = [0] * numCourses
        for p in prerequistes:
            graph[p[1]].append(p[0])
            dep[p[0]] += 1
        q = [i for i in xrange(numCourses) if dep[i] == 0]
        ret = []
        while q:
            tmp = q.pop(0)
            ret.append(tmp)
            for p in graph[tmp]:
                dep[p] -= 1
                if dep[p] == 0:
                    q.append(p)
        return ret if len(ret) == numCourses else []