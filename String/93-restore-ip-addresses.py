# -*- coding: utf-8 -*-

'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Valid IP Address: 4 group of digits, each digits between [0, 255] and no leading 0 (except 0)
'''

class Solution(object):
    def dfs(self, s, path, ans):
        if len(path) == 4 and not s:
            ans.append( ".".join(path) )
            return
        if len(path) >= 4 or not s:
            return
        
        if s[0] == '0':
            self.dfs( s[1:], path + [ s[0] ], ans )
        else:
            for i in range(1, 4):
                if 0 <= int(s[: i]) <= 255:
                    self.dfs( s[i:], path + [s[:i]], ans )
                
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        
        self.dfs( s, [], ans )
        
        return list( set(ans) )