# -*- coding: utf-8 -*-

'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the same character 
but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

# Time and Space: O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        match = {}
        for i in range( len(s) ):
            if s[i] not in match:
                match[ s[i] ] = t[i]
            else:
                if t[i] != match[ s[i] ]:
                    return False
                
        match = {}
        for i in range( len(t) ):
            if t[i] not in match:
                match[ t[i] ] = s[i]
            else:
                if s[i] != match[ t[i] ]:
                    return False
                
        
        return True