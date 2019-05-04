# -*- coding: utf-8 -*-

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def dfs(self, n, ans, path, i, j):
        if i == n and j == n:
            ans.append( path )
            return
        if i > j:
            self.dfs( n, ans, path + ')', i, j + 1 )
        if i < n:
            self.dfs( n, ans, path + '(', i + 1, j )
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        self.dfs( n, ans, "", 0, 0 )
        
        return ans