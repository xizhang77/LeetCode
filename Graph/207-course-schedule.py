# -*- coding: utf-8 -*-

'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites

'''
class Solution(object):
    def dfs(self, graph, node, visited):
        visited[ node ] = -1
        for p in graph[ node ]:
            if visited[p] == -1:
                return False
            if visited[p] == 1:
                continue
            if not self.dfs( graph, p, visited):
                return False
        visited[ node ] = 1
        
        return True
            
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for i in range( numCourses ):
            graph[ i ] = []
        
        for pre in prerequisites:
            p1, p2 = pre
            graph[ p1 ] += [ p2 ]
        
        visited = [0]*numCourses
        
        for i in range( numCourses ):
            if not self.dfs( graph, i, visited ):
                return False

        return True

# Wrong Answer!!!
# UnionFind can only detect cycle in undirected graph

class Solution(object):
    def union(self, parent, p1, p2):
        root_p1, root_p2 = self.find(parent, p1), self.find(parent, p2)
        if root_p1 == root_p2:
            return False
        parent[ root_p1 ] = root_p2
        
        return True
        
    def find(self, parent, p):
        while parent[p] != p:
            p = parent[p]
        
        return p
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        parent = range(numCourses)
        
        for pre in prerequisites:
            p1, p2 = pre
            if not self.union( parent, p1, p2):
                return False
        
        return True