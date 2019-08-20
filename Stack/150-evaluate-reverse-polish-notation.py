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