#!/usr/bin/env python2.7

'''
For a undirected graph with tree characteristics, we can choose any node as the root.
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum
height are called minimum height trees (MHTs). Given such a graph, write a function to find all
the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
'''


class Solution(object):
    def min_height_trees(self, n, edges):
        if n == 1:
            return [0]
        graph = [[] for i in xrange(n)]
        degrees = [0] * n
        for e in edges:
            x, y = e[0], e[1]
            graph[x].append(y)
            degrees[x] += 1
            graph[y].append(x)
            degrees[y] += 1

        q = []
        for i in xrange(n):
            if degrees[i] == 1:
                q.append(i)

        while n > 2:
            tmp = []
            for i in q:
                degrees[i] = 0
                n -= 1
                for j in graph[i]:
                    degrees[j] -= 1
                    if degrees[j] == 1:
                        tmp.append(j)
            q = tmp
        return q