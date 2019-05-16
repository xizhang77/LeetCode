# -*- coding: utf-8 -*-

'''
Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it 
using only constant space complexity?
'''

# Solution 1: Hash Table ( return keys with count == 1 )

# Solution 2: Bit Manipulation

'''
这道题和136-single-number类似，首先全体XOR，得到两个数的异或；
因为两个数字不同，所以二进制中肯定有一位不相等（ 一个数是1 另一个数是0 ）
通过一个MASK从右到左找到不同的那一位
之后再做一遍全体异或，如果
所有这一位和mask不同的（num&mask == 0）数字和num1 异或
所有这一位和mask相同的（num&mask == 1）数字和num2 异或
因为除了这两个数字，其余的数字都出现了两边
因此全体异或之后，num1和num2中分别留下的就是所要找的数字
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        
        for num in nums:
            xor ^= num
        
        mask = 1
        
        while xor & mask == 0:
            mask <<= 1
        
        num1, num2 = 0, 0
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]