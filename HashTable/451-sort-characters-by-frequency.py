# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/sort-characters-by-frequency/
'''

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap = {}
        
        for char in s:
            if char not in hashmap:
                hashmap[ char ] = 1
            else:
                hashmap[ char ] += 1
        sort = sorted( hashmap.items(), key=lambda x:x[1], reverse = True)
        
        ans = ""
        for val in sort:
            ans += val[0] * val[1]
        
        return ans