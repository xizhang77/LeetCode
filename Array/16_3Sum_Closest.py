# -*- coding: utf-8 -*-
'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

# Time: O(n^2); Space: O(n) if created a new sorted list. Otherwise O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = float('inf')
        
        nums = sorted( nums )
        
        for i in range(len(nums) - 2):
            p, q = i+1, len(nums) - 1
            
            while p < q:
                temp = nums[i] + nums[p] + nums[q]
                
                if abs( temp - target ) < abs( ans - target ):
                    ans = temp
                if temp == target:
                    return temp
                
                if temp < target:
                    p += 1
                else:
                    q -= 1
                    
            if nums[i] > target and ans != float('inf'):
                break
                    
                    
        return ans