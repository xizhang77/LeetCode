# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/can-i-win/

Reference: https://www.cnblogs.com/grandyang/p/6103525.html
'''

# DFS中的mask和visited都是用来用状态记录的，标记从 0 ~ maxn 目前被使用的情况
class Solution(object):
    def dfs(self, maxn, target, hashmap, visited ):
        if visited in hashmap:
            return hashmap[ visited ]
        
        for i in range( maxn ):
            mask = (1 << i)
            if not (mask & visited):
                if (target <= i + 1) or (not self.dfs( maxn, target - (i+1), hashmap, mask|visited )):
                    hashmap[ visited ] = True
                    return True
        hashmap[ visited ] = False
        return False
        
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger >= desiredTotal:
            return True
        
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        
        hashmap = {}
        
        return self.dfs( maxChoosableInteger, desiredTotal, hashmap, 0 )