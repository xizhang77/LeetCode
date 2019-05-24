# -*- coding: utf-8 -*-

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

# Soluiton 1: LTE...
class Solution(object):
    def isUgly(self, num):
        if num == 0:
            return False
        
        while num != 1:
            if num % 2 == 0:
                num = num/2
            elif num % 3 == 0:
                num = num/3
            elif num % 5 == 0:
                num = num/5
            else:
                return False  
        return True
    
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 1
        count = 1
        while count < n:
            num += 1
            if self.isUgly( num ):
                count += 1
        return num


# Solution 2: DP
# Time & Space: O(n)

'''
Refer: https://blog.csdn.net/XX_123_1_RJ/article/details/82876296

（1）这个可以考虑动态规划的思想，要求第n个数，思考一下，第n个丑数是怎么来的？
	它一定是在第n个丑数之前的n-1个丑数中的一个，乘以2、3、5得来的。
	现在的问题就是，如何从前n-1个丑数中选出那个丑数来，然后又如何确定是乘以2那，还是3 或者是5那？
（2）解决办法，用一个ugly[i]表示第i+1个丑数，维护一系列丑数。
（3）用变量i2记录在ugly[]中出现的第一个丑数，且，这个丑数乘以2 大于ugly[]中最后一个丑数。 
	此时，很显然ugly[i2] * 2就是下一个丑数的备选值，同理选出ugly[i3] * 3、ugly[i5] * 5，
	然后从这三个值里面选择最小的作为下一个丑数。以此类推，直到选出n个来。
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [ 1 ]
        i2 = i3 = i5 = 0
        
        while len(ans) < n:
            while ans[i2]*2 <= ans[-1]:
                i2 += 1
            while ans[i3]*3 <= ans[-1]:
                i3 += 1
            while ans[i5]*5 <= ans[-1]:
                i5 += 1
            ans.append( min( ans[i2]*2, ans[i3]*3, ans[i5]*5) )
        return ans[-1]