# -*- coding: utf-8 -*-

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''

# Solution 1: Runtime: 1212 ms, faster than 5.01% ...
# Check it later for better solution
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """        
        check = Counter( t )
        
        
        stack = []
        ans, length = "", float('inf')
        hashMap = Counter()
        j = 0
        while j < len(s):
            if s[j] in check:
                stack.append( j )
                i = stack[ 0 ]
                if s[j] not in hashMap:
                    hashMap[ s[j] ] = 1
                else:
                    hashMap[ s[j] ] += 1
            
                while s[i] in check and check[ s[i] ] < hashMap[ s[i] ]:
                    stack.pop( 0 )
                    hashMap[ s[i] ] -= 1
                    i = stack[0]
            
            if not ( check - hashMap ) and j - i + 1 < length:
                ans, length = s[i:j+1], j - i + 1
            
            j += 1
        
        return ans