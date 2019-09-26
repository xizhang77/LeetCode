# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/exclusive-time-of-functions/
'''

# Time & Space: O(n)
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0]*n
        stack = []
        prevtime = 0
        for log in logs:
            funcid, func, time = log.split(":")
            if func == 'start':
                if stack:
                    ans[ stack[-1] ] += int(time) - prevtime
                stack.append( int(funcid) )
                prevtime = int( time )
            else:
                ans[ stack[-1] ] += int(time) - prevtime + 1
                stack.pop()
                prevtime = int( time ) + 1
        
        return ans