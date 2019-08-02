# -*- coding: utf-8 -*-

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
# Solution 1
# Time & Space: O(n)
# One-pass
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        
        num = ""
        op = "+"
        
        stack = []
        for i in range( len(s) ):
            char = s[i]
            
            if char in ["+", "-", "*", "/"] or i == len(s) - 1:
                if i == len(s) - 1:
                    num = int( num + char )
                else:
                    num = int(num)
                if op == '+':
                    stack.append( num )
                elif op == '-':
                    stack.append( -num )                
                elif op == '*':
                    prev = stack.pop()
                    stack.append( prev*num )
                else:
                    prev = stack.pop()
                    if prev < 0:
                        stack.append( - ((-prev)/num) )
                    else:
                        stack.append( prev/num )
                op = char
                num = ""
            else:
                num += char
        
        return sum( stack )

# Solution 2: LTE
# Time & Space: O(n)

class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        
        if not s:
            return 0
        
        stack = [ ["", "+"] ]
        
        num = ""
        
        for i in range( len(s) ):
            char = s[i]
            
            if char in ["+", "-", "*", "/" ]:
                stack[-1][0] += num
                stack.append( ["", char] )
                num = ""
            else:
                num += char
        
        stack[-1][0] += num
        
        ans = 0
        
        for item in stack:
            num, op = item
            if op in ["*", "/"]:
                if ans[-1] < 0 and op == '/':
                    ans[-1] = - (-ans[-1]/int(num))
                else:
                    ans[-1] = ans[-1]*int(num) if op == '*' else ans[-1]/int(num)
            else:
                ans = ans + [ int(num) ] if op == '+' else ans + [ -int(num) ]
            # print ans
            
        return sum( ans )

