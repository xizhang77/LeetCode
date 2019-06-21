# -*- coding: utf-8 -*-

'''
Given a non-empty binary search tree and a target value, find the value in the BST 
that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, target):
        if not root:
            return
        if abs( root.val - target ) < abs( self.ans - target ):
            self.ans = root.val
        
        self.dfs( root.left, target )
        self.dfs( root.right, target )
        
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.ans = float('inf')
        
        self.dfs( root, target )
        
        return self.ans
        