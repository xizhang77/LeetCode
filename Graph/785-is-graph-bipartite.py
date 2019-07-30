# -*- coding: utf-8 -*-

'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
'''


# Refer: https://blog.csdn.net/fuxuemingzhu/article/details/82788401
# 染色问题
# Time: O(V+E); 
class Solution(object):
    def dfs(self, edge, graph, hashmap):
        current = set( [edge] )
        flag = 1
        while current:
            nextlevel = set()
            for node in current:
                hashmap[ node ] = 'Red' if flag else 'Blue'
                for e in graph[ node ]:
                    if not hashmap[ e ]:
                        nextlevel.add( e )
                    else:
                        if hashmap[ e ] == hashmap[ node ]:
                            return False
            current = nextlevel
            flag = 1 - flag
        return True
            
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len( graph )
        
        hashmap = {}
        
        for i in range(n):
            hashmap[ i ] = None
        
        
        for i in range( n ):
            if not hashmap[ i ]:
                if not self.dfs( i, graph, hashmap ):
                    return False
        
        return True
        