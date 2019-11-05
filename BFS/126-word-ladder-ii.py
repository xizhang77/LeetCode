# -*- coding: utf-8 -*-

'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict
class Solution(object):
    def getpath(self, begin, end, prevWord, ans, path ):
        if begin == end:
            ans.append( path[::-1] )
            return
        
        for word in prevWord[ end ]:
            self.getpath( begin, word, prevWord, ans, path + [ word ] )
        
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        
        wordList = set(wordList)
        
        curr = set([beginWord])
        
        char = 'abcdefghijklmnopqrstuvwxyz'
        
        prevword = defaultdict( list )
        
        while curr:
            nxt = set()
            
            for word in curr:
                if word in wordList:
                    wordList.remove( word )
            
            stop = 0
            for word in curr:
                for i in range( len(word) ):
                    left = word[:i]
                    right = word[i+1:]
                    for c in char:
                        temp = left + c + right
                        if temp in wordList:
                            nxt.add( temp )
                            prevword[ temp ].append( word )
                        if temp == endWord:
                            stop = 1
            if stop:
                self.getpath( beginWord, endWord, prevword, ans, [ endWord ] )
                break
            
            curr = nxt
        
        return ans