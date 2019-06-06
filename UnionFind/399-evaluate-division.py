# -*- coding: utf-8 -*-

'''
Equations are given in the format A / B = k, 
where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, 
vector<pair<string, string>> queries , where equations.size() == values.size(), 
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result 
in no division by zero and there is no contradiction.
'''

# Solution 1: DFS
class Solution(object):
    def dfs(self, hashMap, start, end, path, cum):
        if start == end:
            self.val = cum
            return
        
        for key in hashMap[ start ]:
            if key not in path:
                val = self.dfs( hashMap, key, end, path + [ key ], cum*hashMap[ start ][ key ])
        
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        hashMap = {}
        
        for i in range( len(equations) ):
            eq, val = equations[i], values[i]
            if eq[0] not in hashMap:
                hashMap[ eq[0] ] = {eq[0]: 1.0}
            hashMap[eq[0]][ eq[1]] = val
            if eq[1] not in hashMap:
                hashMap[ eq[1] ] = {eq[1]: 1.0}
            hashMap[eq[1]][eq[0]] = 1.0/val
                
        ans = []
        for a,b in queries:
            self.val = -1.0
            if a in hashMap and b in hashMap:
                self.dfs( hashMap, a, b, [ a ], 1.0 )
            ans.append( self.val )
        
        return ans


# Solution 2: Union Find
class Solution(object):
    def find(self, hashMap, p):
        val = 1.0
        while p != hashMap[ p ][ 0 ]:
            val *= hashMap[ p ][ 1 ]
            p = hashMap[ p ][ 0 ]
        return p, val
    
    def union(self, hashMap, p, q, val ):
        root_p, val_p = self.find( hashMap, p )
        root_q, val_q = self.find( hashMap, q )
        hashMap[ root_q ] = [ root_p, val*val_p/val_q ]
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        hashMap = {}
        
        for a, b in equations:
            if a not in hashMap:
                hashMap[ a ] = [ a, 1.0 ]
            if b not in hashMap:
                hashMap[ b ] = [ b, 1.0 ]
                
        for i in range( len(values) ):
            self.union( hashMap, equations[i][0], equations[i][1], values[i])
        
        ans = []
        
        for a, b in queries:
            if a not in hashMap or b not in hashMap:
                ans.append( -1 )
            else:
                root_a, val1 = self.find( hashMap, a )
                root_b, val2 = self.find( hashMap, b )
                if root_a == root_b:
                    ans.append( val2/val1 )
                else:
                    ans.append( -1 )
                    
        return ans