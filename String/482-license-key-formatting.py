# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/license-key-formatting/
'''

# Time: O(n)
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-","").upper()
        S = list(S)
        n = len(S)
        i = K
        while i < n:
            S.insert(-i, '-')
            i += 1 + K
            n += 1
        return "".join(S)