# -*- coding: utf-8 -*-
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		if not height:
			return 0

		n = len(height)
		left = [0] * n
		leftMax = 0
		for i in range(n):
			left[i] = leftMax
			if height[i] > leftMax:
				leftMax = height[i]

		ans = 0
		rightMax = 0
		for i in range(n-1, -1, -1):
			print height[i], rightMax, ans
			if height[i] > rightMax:
				rightMax = height[i]
				continue
			if height[i] < min(left[i], rightMax):
				ans += (min(left[i], rightMax) - height[i])

		return ans

obj = Solution()
print obj.trap( [0,1,0,2,1,0,1,3,2,1,2,1] )

# print obj.trap( [2,1,0,1] )