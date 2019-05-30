# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# Time & Space: O(n)
# Worst case: all chars are different except the last two
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        
        check = set()
        i = j = 0
        while j < len(s):
            if s[j] in check:
                while i < j and s[i] != s[j]:
                    check.remove( s[i] )
                    i += 1
                i += 1
            check.add( s[j] )
            ans = max( ans, j - i + 1 )
            j += 1
        return ans