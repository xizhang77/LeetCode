# -*- coding: utf-8 -*-

'''
Given a binary search tree with non-negative values, 
find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 
(or between 2 and 3).
 

Note: There are at least two nodes in this BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return 
        self.dfs( root.left )
        if self.prev != float('inf'):
            self.ans = min( abs( root.val - self.prev ), self.ans)
        self.prev = root.val 
        self.dfs( root.right )
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = self.ans = float('inf')
        self.dfs( root )
        
        return self.ans