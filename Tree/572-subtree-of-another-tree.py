# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/subtree-of-another-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node1, node2):
        if not node1:
            return ( not node2 )
        if not node2:
            return ( not node1 )
        
        if node1.val == node2.val and self.dfs( node1.left, node2.left ) and self.dfs( node1.right, node2.right ):
            return True
        else:
            return False
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        stack = [ s ]
        
        while stack:
            node = stack.pop( 0 )
            if node.val == t.val and self.dfs( node, t ):
                return True
            if node.left:
                stack.append( node.left )
            if node.right:
                stack.append( node.right )
        
        return False