# -*- coding: utf-8 -*-

'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs( self, root ):
        if not root:
            return 0, float('inf'), -float('inf')
        
        left, lmin, lmax = self.dfs( root.left )
        right, rmin, rmax = self.dfs( root.right )
        
        # print left, lmin, lmax, right, rmin, rmax, root.val
        
        if root.left:
            left = left if root.val > lmax else -1
        if root.right:
            right = right if root.val < rmin else -1
        
        if left < 0 or right < 0:
            return -1, -float('inf'), float('inf')
        else:
            self.ans = max( left + right + 1, self.ans )
            return left + right + 1, min(lmin, root.val), max(rmax, root.val)
        
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        self.dfs( root )
        
        return self.ans