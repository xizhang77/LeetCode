# -*- coding: utf-8 -*-

'''
Remove the minimum number of invalid parentheses in order to 
make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''


class Solution(object):
    def dfs(self, s, check_p, remove_p, char ):
        count = 0
        for i in range( check_p, len(s) ):
            if s[i] == char[0]:
                count += 1
            if s[i] == char[1]:
                count -= 1
            if count >= 0:
                continue
            
            for j in range( remove_p, i+1 ):
                if s[j] == char[1] and (j == 0 or s[j-1] != char[1]):
                    self.dfs( s[:j] + s[j+1:], i, j, char )
            return
        
        if char[0] == '(':
            self.dfs( s[::-1], 0, 0, char[::-1] )
        else:
            self.ans.append( s[::-1] )
        
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        
        self.dfs( s, 0, 0, ['(',')'] )
        
        return self.ans