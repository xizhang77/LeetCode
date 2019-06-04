# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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

# BFS
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return root
        
        current = [ root ]
        
        while current:
            nextLevel = []
            for i in range( len(current) ):
                if i + 1 < len(current):
                    current[i].next = current[i+1]
                if current[i].left:
                    nextLevel.append( current[i].left )
                if current[i].right:
                    nextLevel.append( current[i].right )
            current = nextLevel
        
        return root


# DFS 
# [Refer: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space]
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        node = root
        while root and root.left:
            nextLevel = root.left
            while root:
                root.left.next = root.right
                if root.next and root.next.left:
                    root.right.next = root.next.left
                root = root.next
            root = nextLevel
        
        return node