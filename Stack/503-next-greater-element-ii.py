# -*- coding: utf-8 -*-

'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        maxnum = max(nums)
        idx = [i for i in range( len(nums) ) if nums[i] == maxnum ]
        
        stack = [ nums[idx[-1]] ]
        front, end = nums[:idx[-1]], nums[idx[-1]:]
        nums = end + front
        
        # print nums
        
        ans = []
        
        
        for i in range( len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                ans.append( -1 )
            else:
                ans.append( stack[-1] )
            stack.append( nums[i] )
        
        ans = ans[::-1]
        start, end = ans[:len(nums)-idx[-1]], ans[len(nums)-idx[-1]:]

        return end + start