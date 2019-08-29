# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, check):
        if not root:
            return
        check.add( root.val )
        self.dfs( root.left, check )
        self.dfs( root.right, check )
        
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        check = set()
        self.dfs( root, check )
        
        if len(check) <= 1:
            return -1
        
        return sorted( list(check), reverse = False )[1]