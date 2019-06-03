# -*- coding: utf-8 -*-

'''
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null. Return a deep copy of the list.


Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# Time & Space: O(n)
class Solution(object):
    def dfs(self, hashMap, head):
        if not head:
            return
        if head not in hashMap:
            node = Node( head.val, None, None )
            hashMap[ head ] = node
        if head.next:
            if head.next not in hashMap:
                nextNode = Node( head.next.val, None, None )
                hashMap[ head.next ] = nextNode
            hashMap[ head ].next = hashMap[ head.next ]
        if head.random:
            if head.random not in hashMap:
                randNode = Node( head.random.val, None, None )
                hashMap[ head.random ] = randNode
            hashMap[ head ].random = hashMap[ head.random ]
        
        self.dfs( hashMap, head.next )
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        
        hashMap = {}        
        self.dfs( hashMap, head )
        
        return hashMap[ head ]