#!/usr/bin/env python2.7


'''
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root." Besides the root,
each house has one and only one parent house. After a tour,
the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

http://bookshadow.com/weblog/2016/03/13/leetcode-house-robber-iii/
'''

class Solution(object):
    def rob(self, root):
        if root is None:
            return 0
        val_map = dict()
        def solve(root, path):
            if root is None:
                return 0
            if path not in val_map:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:
                    ll, lr = left.left, left.right
                if right:
                    rl, rr = right.left, right.right
                v1 = solve(left, path + 'l') + solve(right, path + 'r')
                v2 = root.val + solve(ll, path + 'll') + solve(lr, path + 'lr') + \
                     solve(rl, path + 'rl') + solve(rr, path + 'rr')
                val_map[path] = max(v1, v2)
            return val_map[path]
        return solve(root, '')
