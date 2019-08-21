# -*- coding: utf-8 -*-

'''
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hashmap = {}
        for i, word in enumerate(words):
            if word not in self.hashmap:
                self.hashmap[ word ] = [ i ]
            else:
                self.hashmap[ word ] += [ i ]
        
        self.check = {}
    
    def distance(self, word1, word2):
        dist = float('inf')
        for i in self.hashmap[ word1 ]:
            for j in self.hashmap[ word2 ]:
                dist = min( dist, abs(i-j))
                
        return dist
    
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 < word2:
            temp = word1 + "/" + word2
        else:
            temp = word2 + "/" + word1
        
        if temp in self.check:
            return self.check[ temp ]
        else:
            self.check[ temp ] = self.distance( word1, word2 )
            return self.check[ temp ]


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)