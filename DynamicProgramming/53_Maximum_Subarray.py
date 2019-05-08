# -*- coding: utf-8 -*-

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

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
# Time: O(nlgn); Space: O(1)

class Solution(object):
    def divideConquer(self, nums, l, r):
        if l > r:
            return -float('inf')
        
        mid = (l + r)/2
        
        temp = leftSum = 0
        for i in range( mid - 1, l - 1, -1):
            temp += nums[i]
            leftSum = max(leftSum, temp)
            
        temp = rightSum = 0
        for j in range( mid + 1, r + 1 ):
            temp += nums[j]
            rightSum = max(rightSum, temp)
        
        left = self.divideConquer( nums, l, mid - 1)
        right = self.divideConquer( nums, mid + 1, r)
        
        return max( leftSum + nums[mid] + rightSum, max(left, right) )
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return self.divideConquer( nums, 0, len(nums) - 1)