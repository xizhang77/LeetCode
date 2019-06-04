# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/clone-graph/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def dfs(self, hashMap, node, visited ):
        if node in visited:
            return
        visited.append( node )
        
        if node not in hashMap:
            hashMap[ node ] = Node( node.val, [] )
            
        for n in node.neighbors:
            if n not in hashMap:
                hashMap[ n ] = Node( n.val, [] )
            hashMap[ node ].neighbors.append( hashMap[ n ] )
            self.dfs( hashMap, n, visited )
            
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        hashMap = {}
        self.dfs( hashMap, node, [] )
        
        return hashMap[ node ]