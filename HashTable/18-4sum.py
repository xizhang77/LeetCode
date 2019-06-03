# -*- coding: utf-8 -*-

'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

# Solution 1: Two Pointer
# Time: O(n^2 * logn); Space: O(1)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums, reverse = False)
        
        for i in range( len(nums) ):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]
                p, q = j + 1, len(nums) - 1
                
                while p < q:
                    if temp + nums[p] + nums[q] < target:
                        p += 1
                    elif temp + nums[p] + nums[q] > target:
                        q -= 1
                    else:
                        if [nums[i],nums[j],nums[p],nums[q]] not in ans:
                            ans.append( [nums[i],nums[j],nums[p],nums[q]] )
                        p += 1
                        q -= 1

        return ans

# Solution 2: Hash Table
# Time: O(n^2); Space: O(n^2)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        nums.sort( reverse = False )
        n = len(nums)
        
        hashMap = {}
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] not in hashMap:
                    hashMap[ nums[i] + nums[j] ] = [ (i, j) ]
                else:
                    hashMap[ nums[i] + nums[j] ] += [ (i, j) ]
                    
        
        for i in range( n ):
            for j in range( i+1, n-2 ):
                T = target - ( nums[i] + nums[j] )
                if T in hashMap:
                    for p, q in hashMap[T]:
                        if p > j and [ nums[i], nums[j], nums[p], nums[q]] not in ans:
                            ans.append( [ nums[i], nums[j], nums[p], nums[q]] )
        
        return ans