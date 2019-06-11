# -*- coding: utf-8 -*-

'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

# Time: O(n/2) = O(n)
class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = set('abcdefghijklmnopqrstuvwxyz0123456789')
        if not s:
            return True
        
        i, j = 0, len(s) - 1
        
        while i < j:
            while i < j and s[i].lower() not in check:
                i += 1
            while i < j and s[j].lower() not in check:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True



class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = set('abcdefghijklmnopqrstuvwxyz0123456789')
        
        newS = [ c.lower() for c in s if c.lower() in check ]
        
        return newS == newS[::-1]