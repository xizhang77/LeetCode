# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 
        
        stack = []
        
        for val in tokens:
            if val in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()
                if val == '+':
                    stack.append( num2+num1 )
                elif val == '-':
                    stack.append( num2-num1 )
                elif val == '*':
                    stack.append( num2*num1 )
                else:
                    if num1*num2 < 0:
                        stack.append( -(abs(num2)/abs(num1)) )
                    else:
                        stack.append( abs(num2)/abs(num1) )
            else:
                stack.append( int(val) )
                
        return stack[0]


# Solution 2
# Time: O(n); Space: O(1) [no extra space needed]
# However, during practice, it's much slower than solution 1 because the size changes over time
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        i = 0
        while i < len(tokens):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                i += 1
                continue
            
            i -= 2
            num1 = int( tokens.pop(i) )
            num2 = int( tokens.pop(i) )
            
            if tokens[i] == '+':
                tokens[i] = str( num1 + num2 )
            elif tokens[i] == '-':
                tokens[i] = str( num1 - num2 )
            elif tokens[i] == '*':
                tokens[i] = str( num1*num2 )
            else:
                sign = 1
                if num1 * num2 < 0:
                    sign = - 1
                num1, num2 = abs(num1), abs(num2)
                tokens[i] = str( sign * (num1/num2) )
            
            
            # print tokens
        
        return int( tokens[0] )