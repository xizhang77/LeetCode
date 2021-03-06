# -*- coding: utf-8 -*-

'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
'''


class Solution(object):
    def find(self, p):
        while self.parent[ p ] != p:
            p = self.parent[ p ]
        return p
    
    def union(self, p, q):
        root_p, root_q = self.find( p ), self.find( q )
        if root_p == root_q:
            return False
        self.count -= 1
        self.parent[ root_q ] = root_p
        
        return True
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        self.parent = range( n )
        self.count = n
        
        for edge in edges:
            if not self.union( edge[0], edge[1] ):
                return False
        
            
        return self.count == 1
        
        
        