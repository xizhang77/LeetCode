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
        
        ans = -float('inf')
        _max = _min = 1
        
        for num in nums:
            new_min = min( num, _min*num, _max*num )
            new_max = max( num, _max*num, _min*num )

            ans = max(new_max, ans)
            _max, _min = new_max, new_min
            
        return ans