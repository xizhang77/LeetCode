# -*- coding: utf-8 -*-

'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len( nums )
        self.segment = [0]*(2*self.n)
        
        for i in range( self.n ):
            self.segment[ self.n + i ] = nums[i]
            
        for i in range( self.n-1, 0, -1 ):
            self.segment[ i ] = self.segment[ 2*i ] + self.segment[ 2*i+1]
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        idx = self.n + i 
        diff = val - self.segment[ idx ] 
        while idx != 0:
            self.segment[ idx ] += diff
            idx = idx/2
        
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ans = 0
        i += self.n
        j += self.n
        
        while i <= j:
            if i%2 == 1:
                ans += self.segment[ i ]
                i += 1
            if j%2 == 0:
                ans += self.segment[ j ]
                j -= 1
            i = i/2
            j = j/2
            
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)