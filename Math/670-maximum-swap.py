# -*- coding: utf-8 -*-

'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''

# Time: O(nlogn) (dominate by sorting function)
# Space: O(n) (dp array)

from collections import defaultdict
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str( num ))
        
        if len(nums) == 1 or nums == sorted( nums, reverse=True):
            return num
        
        n = len(nums)
        dp = [0]*n
        currmax = 0
        
        for i in range(n-1,-1,-1):
            currmax = max( nums[i], currmax )
            dp[i] = currmax
                
        for i in range( n - 1 ):
            if dp[i] > nums[i]:
                idx = [ j for j in range(i+1,n) if nums[j] == dp[i] ]
                k = idx[-1]
                nums[i], nums[k] = nums[k], nums[i]
                
                return int( "".join(nums) )
        