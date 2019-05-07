# -*- coding: utf-8 -*-

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

# Time & Space: O(n)
class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        left = [0]*(n+1)
        right = [0]*(n+1)
        
        ans = 0
        
        for i in range( len(height) ):
            left[i+1] = max(left[i], height[i])
            
        for i in range( len(height) - 1, -1, -1):
            right[i] = max(right[i+1], height[i] ) 
            
        for i in range( len(height) ):
            ans += max( 0, min(left[i], right[i]) - height[i])
        
        return ans

# [Faster Version] Time & Space: O(n)
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        left = 0
        right = [0]*(n+1)
        
        ans = 0
            
        for i in range( len(height) - 1, -1, -1):
            right[i] = max(right[i+1], height[i] ) 
            
        for i in range( len(height) ):
            left = max( left, height[i] )
            ans += max( 0, min(left, right[i]) - height[i])
        
        return ans

# [AC version with Two Pointer] Time: O(n); Space: O(1)
class Solution3(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0 , len(height) - 1
        
        ans = 0
        
        left, right = 0, 0
        
        while i < j:
            left = max( left, height[i] )
            right = max( right, height[j] )
            
            if left < right:
                ans += ( left - height[i] )
                i += 1
            else:
                ans += ( right - height[j] )
                j -= 1
        
        return ans