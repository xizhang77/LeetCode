# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/find-and-replace-in-string/
'''

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        listS = list(S)
        
        for i in range( len(indexes) ):
            idx, l = indexes[i], len( sources[i] )
            if S[idx:idx+l] == sources[i]:
                listS[idx] = targets[i]
                for j in range(idx+1, idx+l):
                    listS[j] = ""
        
        return "".join(listS)