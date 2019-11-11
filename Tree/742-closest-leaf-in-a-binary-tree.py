# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):
    def retrival(self, node, parent, leaf, hashmap ):
        if parent and node:
            hashmap[ parent.val ].append( node.val )
            hashmap[ node.val ].append( parent.val )
        
        if not node.left and not node.right:
            leaf.add( node.val )
            return
        
        if node.left:
            self.retrival( node.left, node, leaf, hashmap )
        if node.right:
            self.retrival( node.right, node, leaf, hashmap )
        
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        hashmap = defaultdict( list )
        leaf = set()
        
        self.retrival( root, None, leaf, hashmap )
        
        if len( leaf ) == 1:
            return list(leaf)[0]
        
        curr = set([ k ])
        visited = set( [k] )
        
        while True:
            nxt = set()
            for val in curr:
                nxt |= set([ x for x in hashmap[ val ] if x not in visited ])
                if val in leaf:
                    return val
            visited |= curr
            curr = nxt
