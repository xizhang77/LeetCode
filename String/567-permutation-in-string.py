# -*- coding: utf-8 -*-

'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

# Time: O(n); Space: O(m)
# m: len(s1); n: len(s2)
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m > n:
            return False
        if m == n:
            return sorted(s1) == sorted(s2)
        
        check = Counter( s1 )
        temp = Counter( s2[:m-1] )
        
        for i in range(m-1, n):
            # print s2[i], temp
            if s2[i] in temp:
                temp[ s2[i] ] += 1
            else:
                temp[ s2[i] ] = 1
            
            if temp == check:
                return True
            
            temp[ s2[i-m+1] ] -= 1
            if temp[ s2[i-m+1] ] == 0:
                del temp[ s2[i-m+1] ]
        
        
        return False
            
        