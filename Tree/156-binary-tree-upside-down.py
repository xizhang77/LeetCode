# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/binary-tree-upside-down/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import OrderedDict
class Solution(object):
    def dfs(self, node, parent):
        if not node:
            return
        self.dfs( node.left, node )
        self.hashmap[ node ] = parent
        
        
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.hashmap = OrderedDict()
        self.dfs( root, None )
        
        ans = self.hashmap.keys()[0]
        p = ans
        
        for node in self.hashmap:
            if p == root:
                break
            p.left = self.hashmap[ node ].right
            p.right = self.hashmap[ node ]
            self.hashmap[ node ].left = None
            self.hashmap[ node ].right = None
            p = p.right
            
        return ans
        