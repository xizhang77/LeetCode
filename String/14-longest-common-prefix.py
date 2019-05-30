# -*- coding: utf-8 -*-

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        check = list(strs[0])
        
        for string in strs[1:]:
            length = min( len(check),len(string) )
            check = check[: length]
            for i in range( length ):
                if check[i] != string[i]:
                    check[i] = ""
            if not check or check[0] == '':
                return ""
            
        ans = ""
        i = 0
        while i < len(check) and check[i] != "":
            ans += check[i]
            i += 1
            
        return ans