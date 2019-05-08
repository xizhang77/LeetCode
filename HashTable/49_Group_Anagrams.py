# -*- coding: utf-8 -*-

'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''

# Time & Space: O(m*n)
# n: length of strs; m: maximum length of str in strs
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = {}
        
        for item in strs:
            temp = "".join( sorted(item) )
            if temp not in hashMap:
                hashMap[ temp ] = [ item ]
            else:
                hashMap[ temp ] += [ item ]
        
        return hashMap.values()