# -*- coding: utf-8 -*-

'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''

'''
Refer: https://blog.csdn.net/XX_123_1_RJ/article/details/81638353

[真的好难啊…看了很多分析才算勉强理解了…]

这道题其实更多的考察了divide&conquer，dp是比较经典的2D自底向上结构

'''

# Time & Space: O(n^2)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [ 1 ] + nums + [ 1 ]
        n = len( nums )
        
        dp = [ [0]*n for _ in range( n ) ]
        
        for k in range( 2, n ):
            for left in range( n - k ):
                right = left + k
                for i in range( left + 1, right ):
                    dp[left][right] = max( dp[left][right], dp[left][i] + nums[left]*nums[i]*nums[right] + dp[i][right])
        
        return dp[0][n-1]