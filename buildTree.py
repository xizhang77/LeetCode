# -*- coding: utf-8 -*-

'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs( self, preorder, inorder):
        if not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        root.left = self.dfs( preorder, inorder[:idx])
        root.right = self.dfs( preorder, inorder[idx+1:])
        
        return root
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs( preorder, inorder )