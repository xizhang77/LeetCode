# -*- coding: utf-8 -*-

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time: O(n)
# Space: O(1)
class Solution(object):
    def dfs(self, root, path, sum):
        if not root:
            return
        
        if not root.left and not root.right:
            if path + root.val == sum:
                self.ans = True
        
        if root.left:
            self.dfs( root.left, path + root.val, sum )
        if root.right:
            self.dfs( root.right, path + root.val , sum )
            
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ans = False
        
        self.dfs( root, 0, sum )
        
        return self.ans

# [More elegant way, no extra function needed]
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and sum == root.val:
            return True
        
        return self.hasPathSum( root.left, sum - root.val) or self.hasPathSum( root.right, sum - root.val)