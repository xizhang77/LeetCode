# -*- coding: utf-8 -*-

'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution(object):
    def compare(self, num1, num2):
        num1, num2 = str(num1), str(num2)
        if int( num1 + num2 ) > int( num2 + num1 ):
            return True
        else:
            return False
        
    def solver(self, nums):
        if not nums:
            return [ ]
        target = nums[0]
        first = []
        last = []
        same = 1
        for num in nums[1:]:
            if target == num:
                same += 1
                continue
            if self.compare( target, num ):
                last.append( num )
            else:
                first.append( num )
        return self.solver( first ) + [ str(target) ]*same + self.solver( last )
            
        
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        if len( set(nums) ) == 1 and nums[0] == 0:
            return "0"
                
        sortNum = self.solver( nums )
        
        return "".join( sortNum )