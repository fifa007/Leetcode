#!/usr/bin/python2.7

'''
iterative solution for symmetric tree
'''

import Queue
import data_structure

class Solution(object):

    def is_symmetric_tree_helper(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        else:
            q1 = Queue.Queue()
            q1.put(root1)
            q2 = Queue.Queue()
            q2.put(root2)
            while not q1.empty() and not q2.empty():
                t1 = q1.get()
                t2 = q2.get()
                if t1.val != t2.val:
                    return False
                if t1.left is not None:
                    if t2.right is None:
                        return False
                    q1.put(t1.left)
                    q2.put(t2.right)
                else:
                    if t2.right is not None:
                        return False
                if t1.right is not None:
                    if t2.left is None:
                        return False
                    q1.put(t1.right)
                    q2.put(t2.left)
                else:
                    if t2.left is not None:
                        return False
            return True

    def is_symmetric(self, root):
        if root is None:
            return True
        return self.is_symmetric_tree_helper(root.left, root.right)

if __name__ == "__main__":
    sol = Solution()
    r1 = data_structure.tree_node(1)
    r1.left = data_structure.tree_node(2)
    r1.right = data_structure.tree_node(3)
    print sol.is_symmetric(r1)