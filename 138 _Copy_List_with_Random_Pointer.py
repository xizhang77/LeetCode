'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def dfs(self, node, hashMap):
        if not node:
            return
        
        if node not in hashMap:
            hashMap[ node ] = RandomListNode(node.label)
        
        if node.next:
            if node.next not in hashMap:
                hashMap[ node.next ] = RandomListNode(node.next.label)
            hashMap[ node ].next = hashMap[ node.next ]
        
        if node.random:
            if node.random not in hashMap:
                hashMap[ node.random ] = RandomListNode(node.random.label)
            hashMap[ node ].random = hashMap[ node.random ] 
        
        self.dfs( node.next, hashMap )
            
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        
        hashMap = {}
        
        self.dfs( head, hashMap )
        
        return hashMap[ head ]