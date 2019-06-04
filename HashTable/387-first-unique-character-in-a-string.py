# -*- coding: utf-8 -*-

'''
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

# Time & Space: O(n)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        
        for i in range( len(s) ):
            if s[i] not in count:
                count[ s[i] ] = [ 1, i ]
            else:
                count[ s[i] ][0] += 1
        
        ans = [ val[1] for val in count.values() if val[0] == 1 ]
        
        if not ans:
            return -1
        else:
            return min( ans )