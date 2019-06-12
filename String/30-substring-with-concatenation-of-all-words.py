# -*- coding: utf-8 -*-

'''
You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words 
exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''


class Solution1(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        
        n = len( words[0] )
        check = []
        
        i = 0
        while i < len(s):
            if s[i:i+n] in words:
                check.append( [i,s[i:i+n]] )
            i += 1
        
        ans = []
        
        if len(check) < len(words):
            return ans
        
        words = sorted(words)
        
        for i in range( len(check) ):
            stack = []
            for j in range( i, len(check) ):
                if not stack or check[j][0] == n + idx:
                    stack.append( check[j][1] )
                    idx = check[j][0]
                
                if len(stack) == len( words ):
                    if sorted(stack) == words:
                        ans.append( check[i][0] )
                    break
            
        return ans