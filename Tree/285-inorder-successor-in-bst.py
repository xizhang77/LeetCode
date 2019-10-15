# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/inorder-successor-in-bst/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postOrder(self, root, p):
        if not root or self.ans:
            return
        self.postOrder( root.right, p )
        if root == p:
            self.ans = self.prev
            return
        self.prev = root
        self.postOrder( root.left, p )
        
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        self.prev = None
        self.postOrder( root, p )
        
        return self.ans