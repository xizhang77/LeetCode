# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        
        current = [ root ]
        
        while current:
            nextlevel = []
            
            for i in range( len(current) - 1 ):
                current[i].next = current[i+1]
            current[-1].next = None
            
            for node in current:
                if node.left:
                    nextlevel.append( node.left )
                if node.right:
                    nextlevel.append( node.right )
            
            current = nextlevel
        
        return root