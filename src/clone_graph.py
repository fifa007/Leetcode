#!/usr/bin/env python2.7


'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import src.data_structure

class Solution(object):
    def clone_graph(self, node):
        if node is None:
            return None
        q = [node]
        d = dict()
        ret = src.data_structure.UndirectedGraphNode(node.label)
        d[node] = ret
        while q:
            tmp = q.pop(0)
            neighbor_list = tmp.neighbors
            for item in neighbor_list:
                if item in d:
                    d[tmp].neighbors.append(d[item])
                else:
                    new_node = src.data_structure.UndirectedGraphNode(item.label)
                    d[item] = new_node
                    d[tmp].neighbors.append(d[item])
                    q.append(item)
        return ret
