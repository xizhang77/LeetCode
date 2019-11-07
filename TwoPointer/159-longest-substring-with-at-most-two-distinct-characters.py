
'''
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''

from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        
        if len( set(s) ) <= 2:
            return len(s)
        
        check = defaultdict( list )
        
        i = j = 0
        
        while j < len(s):
            if s[j] not in check and len(check) == 2:
                temp = sorted( check.items(), key=lambda x:x[1] )
                val, idx = temp[0]
                i = idx + 1
                del check[ val ]
                     
            ans = max( ans, j - i + 1 )
            check[ s[j] ] = j
            j += 1
            
        return ans