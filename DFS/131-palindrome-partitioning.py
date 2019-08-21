# -*- coding: utf-8 -*-

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
# Time: O(n!)
class Solution(object):
    def dfs(self, path, s):
        if not s:
            self.ans.append( path )
            return
        
        for i in range( len(s) ):
            if s[:i+1] == s[:i+1][::-1]:
                self.dfs( path +[ s[:i+1] ], s[i+1: ] )
                
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []
        
        self.dfs( [], s )
        
        return self.ans