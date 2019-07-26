# -*- coding: utf-8 -*-

'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, flag):
        if not root:
            return
        if flag and (not root.left) and (not root.right):
            self.ans += root.val
            return
        
        self.dfs( root.left, True )
        self.dfs( root.right, False )
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs( root, False )
        
        return self.ans