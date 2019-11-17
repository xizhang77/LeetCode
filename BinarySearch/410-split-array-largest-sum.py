# -*- coding: utf-8 -*-

'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

# Binary Search
class Solution(object):
    def cansplit(self, nums, target, m ):
        count = 1
        curr = 0
        for num in nums:
            curr += num
            if curr > target:
                curr = num
                count += 1
            if curr > target or count > m:
                return False
        
        return True
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len( nums )
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = left + (right-left)/2
            
            if self.cansplit( nums, mid, m ):
                right = mid
            else:
                left = mid + 1 
        return left