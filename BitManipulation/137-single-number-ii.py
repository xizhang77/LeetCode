# -*- coding: utf-8 -*-

'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''


'''
ref: https://cloud.tencent.com/developer/article/1131945

    如果是出现两次的话，用一个bit就可以
    比如 b，初始为0
    当5第1次出现时， b=5
    当5第2次出现是， b清空为0，表示b可以去处理其他数字了
    所以，最后 如果 b !=0的话，b记录的就是只出现了一次的那个数字
    
    ->公式就是 b = b xor i  或者 b = b^i


    那么，如果是三次的话，香浓定理，需要用2bits进行记录

    当5第一次出现的时候，b = 5, a=0,  b记录这个数字
    当5第二次出现的时候，b = 0, a=5， a记录了这个数字
    当5第三次出现的时候，b = 0, a=0， 都清空了，可以去处理其他数字了
    所以，如果有某个数字出现了1次，就存在b中，出现了两次，就存在a中，所以返回 a|b

    公式方面 ，上面两次的时候，b清空的公式是 b = b xor i
    而第三次时，b要等于零，而这时a是True，所以再 & 一个a的非就可以，b = b xor & ~a

    -> b = b xor i & ~ a
       a = a xor i & ~ b

'''
# Solution 1: Bit
# Time: O(n); Space: O(1) 
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        
        return one


# Solution 2: Hash Table
# Time & Space: O(n)
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        
        for num in nums:
            if num in hashMap:
                if hashMap[ num ] == 2:
                    del hashMap[ num ]
                else:
                    hashMap[ num ] += 1
            else:
                hashMap[ num ] = 1
        
        return hashMap.keys()[0]
