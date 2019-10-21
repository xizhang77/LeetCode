# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/course-schedule-ii/
'''


# Solution 1: Topological Sort + DFS
from collections import defaultdict
class Solution(object):
    def dfs(self, graph, visited, i, ans):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs( graph, visited, j, ans):
                return False
        ans.append(i)
        visited[i] = 2
        return True
        
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict( list )
        
        for u, v in prerequisites:
            graph[u].append( v )
        
        visited = [0]*numCourses
        ans = []
        for i in range( numCourses ):
            if not self.dfs( graph, visited, i, ans ):
                return []
        
        return ans


# Solution 2: Topological Sort + BFS
from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = defaultdict( list )
        degree = defaultdict( int )
        
        for u, v in prerequisites:
            graph[ v ].append( u )
            degree[u] += 1
        
        
        ans = []
        
        for _ in range( numCourses ):
            # print degree
            flag = 1
            for i in range( numCourses ):
                if degree[i] == 0:
                    flag = 0
                    break
            if flag:
                return []
                
            ans.append( i )
            degree[ i ] -= 1
            for j in graph[ i ]:
                degree[ j ] -= 1
        
        return ans