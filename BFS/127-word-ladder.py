# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/word-ladder/
'''

# Solution 1: BFS [ 692 ms, faster than 13.55% ]
# One can remove the word from wordList instead of add it into check
# Runtime improved to 38.96%
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if not wordList or endWord not in wordList:
            return 0
        
        charset = set('abcdefghijklmnopqrstuvwxyz')
        check = set()
        current = [ beginWord ]
        count = 1
        while current:
            count += 1
            nextlevel = set()
            for word in current:
                check.add( word )
                for i in range( len(word) ):
                    for char in charset:
                        temp = word[:i] + char + word[i+1:]
                        if temp in wordList and temp not in check and temp not in nextlevel:
                            nextlevel.add( temp )  
                        if temp == endWord:
                            return count
            current = nextlevel 
        
        return 0
                            