# -*- coding: utf-8 -*-

'''
On a 2D plane, we place stones at some integer coordinate points.  
Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?


Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000

'''

'''
这道题读明白以后，不是非常难解…就是求无闭环的图一共有多少edge…基本思想是 Disjoint Sets
'''

class Solution(object):
    def find(self, parent, p):
        if p not in parent:
            parent[ p ] = p
        while p != parent[p]:
            p = parent[p]
        return p
    
    def union(self, parent, p, q):
        root_p, root_q = self.find( parent, p), self.find( parent, q)
        if root_p == root_q:
            self.count -= 1
            return
        parent[ root_q ] = root_p
        
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        self.count = 0
        parent = {}
        
        edge = {}
        
        n = len( stones )
        
        for i in range( n ):
            x, y = stones[i]
            if x not in edge:
                edge[ x ] = [ y ]
            else:
                edge[ x ] += [ y ]
            if y + 10000 not in edge:
                edge[ 10000 + y ] = [ x ]
            else:
                edge[ 10000 + y ] += [ x ]
        
        
        for key in edge:
            if len( edge[ key ] ) > 1:
                if key >= 10000:
                    for i in range( len( edge[key] ) - 1 ):
                        self.count += 1
                        self.union( parent, (edge[key][i], key-10000), (edge[key][i+1], key-10000) )
                else:
                    for i in range( len( edge[key] ) - 1 ):
                        self.count += 1
                        self.union( parent, (key, edge[key][i]), (key, edge[key][i+1]) )

        
        return self.count
        