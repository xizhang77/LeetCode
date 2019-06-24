# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/verifying-an-alien-dictionary/
'''

from collections import OrderedDict

class Solution(object):
    def check(self, ordermap, word1, word2 ):
        if word1 == word2:
            return True
        
        n1, n2 = len( word1 ), len( word2 )
        i = 0
        while i < n1:
            if i >= n2 or ordermap[ word1[i] ] > ordermap[ word2[i] ]:
                return False
            if ordermap[ word1[i] ] < ordermap[ word2[i] ]:
                return True
            if ordermap[ word1[i] ] == ordermap[ word2[i] ]:
                i += 1
                continue

        
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ordermap = OrderedDict()
        for i, char in enumerate( list(order) ):
            ordermap[ char ] = i
        
        n = len( words )
        
        for i in range( n - 1 ):
            result = self.check( ordermap, words[i], words[i+1] )
            if not result:
                return False
        
        return True
            