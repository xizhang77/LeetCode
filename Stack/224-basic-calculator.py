# -*- coding: utf-8 -*-

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

# Time: O(n)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        
        stack = [ [1, ""] ]
        
        for char in s:
            if char.isdigit():
                stack[-1][1] += char
            elif char == '+':
                stack += [ [1, ""] ]
            elif char == '-':
                stack += [ [-1, ""] ]
            elif char == '(':
                stack += [ [1, ""] ]
            elif char == ')':
                temp = 0
                while stack and stack[-1][1] != "":
                    sign, num = stack.pop()
                    temp += sign*int(num)
                stack[-1][1] += str(temp)
            
        return sum( val[0]*int(val[1]) for val in stack if val != "")