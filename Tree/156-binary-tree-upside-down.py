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

# Solution 1
class Solution1(object):
    def dfs(self, root, parent, stack):
        if not root:
            return
        stack.append( [root, parent ] )
        self.dfs( root.left, root, stack )
        
    def solver(self, stack):
        if not stack:
            return
        
        node, parent = stack.pop()
        if parent:
            node.left = parent.right
            parent.left = None
            parent.right = None
        node.right = self.solver( stack )
        
        return node
        
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        self.dfs( root, None, stack )
        
        return self.solver( stack )


# Solution 2
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
        