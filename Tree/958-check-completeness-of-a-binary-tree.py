# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [ root ]
        empty = False
        while stack:
            node = stack.pop( 0 )
            if not node:
                empty = True
                continue
            
            if empty:
                return False
            
            stack.append( node.left )
            stack.append( node.right )
        
        return True
        