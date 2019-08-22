# -*- coding: utf-8 -*-

'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s.
 If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

# Solution 1
# Time: O(n); Space: O(1)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        
        subsum = 0
        ans = float('inf')
        
        i = 0
        for j in range( len(nums) ):
            subsum += nums[j]
            
            while subsum >= s:
                ans = min( ans, j - i + 1 )
                subsum -= nums[i]
                i += 1
        
        return ans