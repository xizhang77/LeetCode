# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/redundant-connection/
'''

# Solution 1: Union Find
class Solution(object):
    def find(self, hashmap, p):
        if p not in hashmap:
            hashmap[ p ] = p
            
        while p != hashmap[ p ]:
            p = hashmap[ p ]
        return p
    
    def union(self, hashmap, p, q):
        root_p, root_q = self.find( hashmap, p ), self.find( hashmap, q )
        if root_p == root_q:
            return False
        hashmap[ root_q ] = root_p
        return True
        
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        hashmap = {}
        
        for edge in edges:
            if not self.union( hashmap, edge[0], edge[1] ):
                return edge

                