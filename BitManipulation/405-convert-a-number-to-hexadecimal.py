# -*- coding: utf-8 -*-

'''
Given an integer, write an algorithm to convert it to hexadecimal. 
For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, 
it is represented by a single zero character '0'; otherwise, 
the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
'''

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        hashmap = {0: "0", 1: "1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        
        mask = 1
        nums = []
        if num > 0:
            for _ in range(31):
                nums.append( 1 if num&mask else 0 )
                mask <<= 1
            nums += [0]
        else:
            num = abs(num) - 1
            for _ in range(31): 
                nums.append( 0 if num&mask else 1 )
                mask <<= 1
            nums += [1]
        
        ans = []
        for i in range(0, 32, 4):
            temp = nums[i:i+4]
            res = 0
            for d in range(4):
                res += temp[d]*(2**d)
            ans.append( hashmap[ res ] )
        
        while ans and ans[-1] == '0':
            ans.pop()
        
        return "".join(ans[::-1])