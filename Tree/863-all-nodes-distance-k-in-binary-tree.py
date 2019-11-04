# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def connect(self, parent, child, _map):
        if parent and child:
            _map[ parent.val ].append( child.val )
            _map[ child.val ].append( parent.val )
        
        if child.left:
            self.connect( child, child.left, _map )
        if child.right:
            self.connect( child, child.right, _map )
            
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        _map = defaultdict( list )
        self.connect( None, root, _map )
        
        
        curr = [ target.val ]
        visited = set( [target.val] )
        for _ in range(K):
            nxt = []
            for node in curr:
                nxt += [ x for x in _map[ node ] if x not in visited ]

            visited |= set(nxt)
            curr = nxt
        
        return list( curr )