# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/house-robber-iii/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time and Space: O(n) where n is number if nodes
class Solution(object):
    def dfs(self, root):
        if not root:
            return 0, 0
        
        left, subleft = self.dfs( root.left )
        right, subright = self.dfs( root.right )
        
        woroot = left + right
        
        return max( root.val+subleft+subright, woroot ), woroot
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs( root )[0]