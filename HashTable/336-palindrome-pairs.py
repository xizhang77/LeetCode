# -*- coding: utf-8 -*-

'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''

# Solution 1: LTE...

class Solution(object):
    def palindrome(self, word1, word2 ):
        if word1 == word2[::-1]:
            return True
        word = word1 + word2
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        
        for i in range( len(words) ):
            for j in range( len(words) ):
                if i == j:
                    continue
                if self.palindrome( words[i], words[j] ):
                    ans.append( [i,j] )
        
        return ans


# Time: O( k * n^2) 
# k: number of words; n: longest length of word
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {w : i for i, w in enumerate(words)}
        
        ans = []
        
        for word in wmap:
            if word == "":
                continue
                
            if word == word[::-1] and "" in wmap:
                ans.append( [ wmap[word], wmap[""] ])
                ans.append( [ wmap[""], wmap[word] ])
                
            if word != word[::-1] and word[::-1] in wmap:
                ans.append( [ wmap[word], wmap[ word[::-1] ] ] )
            
            for i in range( 1, len(word) ):
                left, right = word[:i], word[i: ]
                if right == right[::-1] and left[::-1] in wmap:
                    ans.append( [ wmap[word], wmap[left[::-1]]] )
                if left == left[::-1] and right[::-1] in wmap:
                    ans.append( [ wmap[right[::-1]], wmap[ word ] ])
    
        return ans