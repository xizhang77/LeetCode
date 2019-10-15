# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
'''

# Time & Space: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return 0, None
        l, lnode = self.dfs( root.left )
        r, rnode = self.dfs( root.right )
        
        if l > r:
            return l + 1, lnode
        elif l < r:
            return r + 1, rnode
        else:
            return l + 1, root
        
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.dfs( root )[1]
        