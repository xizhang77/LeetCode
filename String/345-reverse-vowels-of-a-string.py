# -*- coding: utf-8 -*-

'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".


'''

# Time: O(n) Space: O(n)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        i, j = 0, len(s) - 1
        
        while i < j:
            while i < j and s[i].lower() not in vowels:
                i += 1
            while i < j and s[j].lower() not in vowels:
                j -= 1
            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)