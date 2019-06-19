# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/simplify-path/
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        
        path = [ val for val in path if val != ""]
        
        stack = []
        
        for val in path:
            if val == "..":
                if stack:
                    stack.pop()
            elif val == ".":
                continue
            else:
                stack.append( val )
        
        return "/" + "/".join(stack)