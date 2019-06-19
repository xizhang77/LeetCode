# -*- coding: utf-8 -*-

'''
Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

# Solution 1: DP
# Time and Space: O(n)
class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if nums[0] == 0:
            return n == 1
        
        dp = [ False ] * n
        dp[0] = True
        
        for i in range( n - 1 ):
            if i + nums[i] < n - 1 and dp[ i + nums[i] ]:
                continue
            if not dp[i]:
                continue
            if i + nums[i] > n - 1:
                return True
            dp[i+1: min(nums[i]+i+1, n)] = [True]* min(nums[i], n-i)
            
        return dp[-1]


# Solution 2: Greedy
# Time: O(n); Space: O(1)
class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if nums[0] == 0:
            return n == 1
        
        maxIndex = nums[0]
        for i in range( n ):
            if i > maxIndex:
                return False
            if maxIndex >= n - 1:
                return True
            maxIndex = max( maxIndex, i + nums[i] )
            
        return False