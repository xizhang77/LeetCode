# -*- coding: utf-8 -*-

'''
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

Follow up:

If this function is called many times, how would you optimize it?


'''

# Solution 1: Convert to string
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = str( bin(n) ).split('b')[1]
        
        return sum([ 1 for char in string if char == '1'])


# Solution 2: Bit Manipulation [Using mask]
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        mask = 1
        
        for i in range(32):
            if n&mask:
                count += 1
            
            mask <<= 1
        
        return count

# Solution 3: Bit Manipulation [Tricky]
# Refer: https://leetcode.com/problems/number-of-1-bits/solution/

# Speed up a little bit compare to solution 1&2 (Worst case O(32); Most of time, better than O(32))
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        while n:
            count += 1
            n &= (n-1)
        
        return count
