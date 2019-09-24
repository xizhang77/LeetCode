# -*- coding: utf-8 -*-

'''
Given an array of integers nums and a positive integer k, 
find whether it's possible to divide this array into k non-empty subsets 
whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets 
(5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

# Time: O(k^N); Space: O(k)
# For DFS, we make k calls from each call.
class Solution(object):
    def dfs(self, nums, path):
        if not nums:
            return True
        
        val = nums.pop()
        
        for i in range( len(path) ):
            if path[i] >= val:
                path[i] -= val
                if self.dfs( nums, path ):
                    return True
                path[i] += val
        nums.append( val )
        
        return False
        
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums)%k != 0:
            return False
        
        target = sum(nums)/k
        
        nums = sorted(nums)
        if nums[-1] > target:
            return False
        
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        
        return self.dfs( nums, [target]*k )