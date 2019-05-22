# -*- coding: utf-8 -*-

'''
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

# Time: O(n); Space: O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax, currMin = 1, 1 
        
        ans = -float('inf')
        
        for num in nums:            
            temp = currMax
            
            currMax = max( num, num*currMax, num*currMin)
            currMin = min( num, num*temp, num*currMin )
            
            ans = max( ans, currMax )
        
        return ans