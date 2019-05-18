# -*- coding: utf-8 -*-

'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, start, end):
        if start == end:
            return [ None ]
        ans = []
        
        for val in range(start, end):
        
            left = self.dfs( start, val )
            right = self.dfs( val + 1, end )
        
            for lnode in left:
                for rnode in right:
                    node = TreeNode( val )
                    node.left = lnode
                    node.right = rnode
                    ans.append( node )
        return ans
        
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        return self.dfs( 1, n+1 )