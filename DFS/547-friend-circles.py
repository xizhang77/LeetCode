# -*- coding: utf-8 -*-

'''
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, 
and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
'''

# Solution 1: DFS (Similar to # of island)
# Time: O(n^2)
class Solution(object):
    def dfs(self, M, i, n, visited):
        if i in visited:
            return
        for j in range( n ):
            if M[i][j] == 1:
                M[i][j] = M[j][i] = 0
                self.dfs(M, j, n, visited + [i] )
            
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        ans = 0
        n = len(M)
        
        for i in range( n ):
            for j in range( n ):
                if M[i][j] == 1:
                    ans += 1
                    M[i][j] = M[j][i] = 0
                    self.dfs(M, i, n, [])
        
        return ans

# Solution 2: Union find
# 2-1: need one more for foop at the end to finally merge everything
class Solution(object):
    def find(self, parent, p):
        while p != parent[p]:
            p = parent[p]
        return p
    
    def union(self, parent, p, q):
        id_p, id_q = self.find(parent, p), self.find(parent, q)
        if id_p == id_q:
            return
        parent[ id_q ] = id_p
        return
    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        n = len(M)
        parent = range( n )
        
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j:
                    M[i][j] = M[j][i] = 0
                    self.union(parent, i, j)
        
        for i in range(n):
            parent[i] = self.find( parent, i )
            
        return len( set(parent) )


# 2-2: one path merge. only count the one without parent.
class Solution(object):
    def find(self, p):
        if self.parent[p] == -1:
            return p
        return self.find( self.parent[p] )
    
    def union(self, p, q):
        id_p, id_q = self.find( p ), self.find( q )
        if id_p == id_q:
            return
        self.parent[ id_q ] = id_p
        
        return
    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        n = len(M) 
        self.parent = [ -1 ] * n
        
        for i in range( n ):
            for j in range( n ):
                if M[i][j] == 1 and i != j:
                    M[i][j] = M[j][i] = 0
                    self.union( i, j )
        
        return sum( [1 for i in range(n) if self.parent[i] == -1 ])
# Solution 3: BFS