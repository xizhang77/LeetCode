# -*- coding: utf-8 -*-

'''
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]

Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

'''

class Solution(object):
    def helper(self, word1, word2):
        n = len(word1)
        check = {}
        for i in range(n):
            if word1[i] not in check:
                check[ word1[i] ] = word2[i]
            else:
                if word2[i] != check[ word1[i] ]:
                    return False
        return True
        
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        n = len(pattern)
        for word in words:
            if self.helper( word, pattern ) and self.helper( pattern, word ):
                ans.append( word )
        
        
        return ans