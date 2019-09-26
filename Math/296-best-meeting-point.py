# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/best-meeting-point/
'''

class Solution(object):
    def distance(self, nums):
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            ans += nums[j] - nums[i]
            i += 1
            j -= 1
        
        return ans
    
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        row = []
        col = []
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if grid[i][j] == 1:
                    row.append( i )
                    col.append( j )
        
        return self.distance( row ) + self.distance( col )