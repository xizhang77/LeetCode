# -*- coding: utf-8 -*-

'''
Given two integers dividend and divisor, divide two integers without using multiplication, 
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

'''

# 不符合题意…不让用乘除和mod…

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if abs(dividend) < abs(divisor):
            return 0
        
        if dividend * divisor > 0:
            dividend, divisor = abs(dividend), abs(divisor)
        else:
            dividend, divisor = - abs(dividend), abs(divisor)
            
        if dividend > 0:
            i, j = 0, dividend
        else:
            i, j = dividend, 0 
        
        while i <= j:
            mid = i + (j-i)/2
            if mid * divisor < dividend:
                i = mid + 1
            elif mid * divisor > dividend:
                j = mid - 1
            else:
                if dividend > 0:
                    return mid if mid <= 2**31 - 1 else 2**31 -1 
                else:
                    return mid if mid >= - 2**31 else -2**31
        
        if dividend > 0:
            return j if j <= 2**31 - 1 else 2**31 -1 
        else:
            return i if i >= - 2**31 else -2**31


# Solution 2:
# Refer: https://blog.csdn.net/danspace1/article/details/86243860
# 用被除数不断地减除数的1倍、2倍、4倍、8倍...

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend * divisor < 0:
            neg = True
        else:
            neg = False

        
        dividend, divisor = abs(dividend), abs(divisor)   
        res = 0
        while dividend >= divisor:
            temp, q = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += q
                temp <<= 1
                q <<= 1
        
        if neg:
            return max( -res, -2**31)
        else:
            return min( res, 2**31-1)