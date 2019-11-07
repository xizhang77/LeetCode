# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def inOrder( self, root ):
        if not root:
            return 
        
        self.inOrder( root.left )
        
        if not self.head:
            self.head = root
            self.tail = root
        else:
            self.tail.right = root
            root.left = self.tail
            self.tail = root
        
        self.inOrder( root.right )
        
        
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.head, self.tail = None, None
        
        self.inOrder( root )
        
        if self.head:
            self.head.left = self.tail
            self.tail.right = self.head
        
        return self.head