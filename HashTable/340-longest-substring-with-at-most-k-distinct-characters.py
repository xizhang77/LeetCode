# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring T that contains 
at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        
        i = j = 0
        
        count = {}
        
        for j in range( len(s) ):
            if s[j] not in count:
                count[ s[j] ] = 1
            else:
                count[ s[j] ] += 1
            
            while len( count ) > k:
                count[ s[i] ] -= 1
                if count[ s[i] ] == 0:
                    del count[ s[i] ]
                
                i += 1
            
            ans = max( ans, j - i + 1 )
        
        
        return ans