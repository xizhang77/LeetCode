# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/validate-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution(object):
    def isValid(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        
        left = self.isValid( root.left, low, root.val )
        right = self.isValid( root.right, root.val, high )
        
        return left and right
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isValid( root.left, -float('inf'), root.val ) and self.isValid( root.right, root.val, float('inf') )