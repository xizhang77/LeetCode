# -*- coding: utf-8 -*-

'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution 
using the divide and conquer approach, which is more subtle.

'''

# [Solution 1 using DP] Time & Space: O(n)
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-float('inf')]
        
        ans = -float('inf')
        
        for num in nums:
            dp.append( max(dp[-1] + num, num))
            ans = max(ans, dp[-1])
        
        return ans

# [Solution 2 using Divide and Conquer]
# Time: O(nlgn)

class Solution(object):
    def div(self, nums):
        if not nums:
            return -float('inf')
        
        mid = len(nums)/2
        
        leftSum = temp = 0
        for i in range( mid-1, -1, -1 ):
            temp += nums[i]
            leftSum = max(leftSum, temp )
        
        rightSum = temp = 0
        for i in range( mid+1, len(nums) ):
            temp += nums[i]
            rightSum = max(rightSum, temp )
        
        left = self.div( nums[:mid] )
        right = self.div( nums[mid+1:])
        
        return max( leftSum + nums[mid] + rightSum, left, right )
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return self.div( nums )