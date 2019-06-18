# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/most-common-word/
'''

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        hashmap = {}
        ans = ""
        count = 0
        for word in paragraph.lower().split():
            if word in banned:
                continue
            if word not in hashmap:
                hashmap[ word ] = 1
            else:
                hashmap[ word ] += 1
                
            if hashmap[ word ] > count:
                count = hashmap[ word ]
                ans = word
        
        
        return ans