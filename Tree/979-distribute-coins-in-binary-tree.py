# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/distribute-coins-in-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time and Space: O(n)
class Solution(object):
    def dfs(self, root ):
        if not root:
            return 0
        left = self.dfs( root.left )
        right = self.dfs( root.right )
        
        self.ans += abs(left) + abs(right)
        
        return root.val + left + right - 1
    
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        self.dfs( root )
        
        return self.ans