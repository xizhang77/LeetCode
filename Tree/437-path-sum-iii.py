# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/path-sum-iii
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, sum, path):
        if not root:
            return
        
        if root.val == sum:
            self.ans += 1
            

        newpath = []
        for val in path:
            newpath.append( val + root.val )
            if val + root.val == sum:
                self.ans += 1
        path = newpath + [ root.val ]
        
        
        self.dfs( root.left, sum, path )
        self.dfs( root.right, sum, path )
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ans = 0
        self.dfs( root, sum, [] )
        
        return self.ans