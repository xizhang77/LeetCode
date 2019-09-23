# -*- coding: utf-8 -*-

'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
'''

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hashmap = {}
        
        idx1 = float('inf')
        idx2 = float('inf')
        
        ans = float('inf')
        
        if word1 == word2:
            idx = [ i for i in range( len(words)) if words[i] == word1 ]
            for i in range( len(idx) - 1 ):
                ans = min( ans, idx[i+1] - idx[i] )
        else:
            for i, word in enumerate(words):            
                if word == word1:
                    idx1 = i
                if word == word2:
                    idx2 = i
                ans = min(ans, abs(idx1 - idx2))
        
        
        return ans