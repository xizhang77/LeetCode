# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/keyboard-row/
'''

# Time: O( n ) where n is the length of words
# Space: O(26)
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        hashMap = {1:set('QWERTYUIOP'), 2:set('ASDFGHJKL'), 3:set('ZXCVBNM')}
        
        ans = []
        
        for word in words:
            for val in hashMap.values():
                if set( word.upper() ) - val == set():
                    ans.append( word )
                    break
        return ans