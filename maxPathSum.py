# -*- coding: utf-8 -*-

'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def dfs(self, root, maxSum):
        if not root:
            return -float('inf')
        left = self.dfs(root.left, self.maxSum)
        right = self.dfs(root.right, self.maxSum)
        
        temp = max( root.val + left, root.val + right, root.val)
        self.maxSum = max([self.maxSum, temp, left, right, left + right + root.val])
        
        return temp

        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -float('inf')
        
        self.dfs(root, self.maxSum)
        
        return self.maxSum