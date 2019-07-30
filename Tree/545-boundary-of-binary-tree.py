# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/boundary-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs( self, root, path ):
        if not root:
            return
        if not root.left and not root.right:
            path.append( root )
            return
        self.dfs( root.left, path )
        self.dfs( root.right, path )
        
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        left = []
        right = []
        
        if not root.left:
            left = [ root ]
        else:
            p = root
            while p:
                left.append( p )
                if p.left:
                    p = p.left
                else:
                    p = p.right
        
        p = root.right
        while p:
            right.append( p )
            if p.right:
                p = p.right 
            else:
                p = p.left
                
        leaf = []
        self.dfs( root, leaf )
        
        temp = left + leaf + right[::-1]
        ans = []
        check = set()
        
        for node in temp:
            if node not in check:
                ans.append( node.val )
                check.add( node )
        
        return ans