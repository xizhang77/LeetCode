# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, level):
        if not self.S:
            return
        i = 0
        while self.S[i] == '-':
            i += 1
        if i != level:
            return
        self.S = self.S[i:]
        
        i = 0
        while i < len(self.S) and self.S[i].isdigit():
            i += 1
        
        node = TreeNode( int(self.S[:i]) )
        self.S = self.S[i:]
        
        node.left = self.dfs( level + 1 )
        node.right = self.dfs( level + 1 )
        
        
        return node
    
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        self.S = S
        return self.dfs( 0 )