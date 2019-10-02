# -*- coding: utf-8 -*-

'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''

# Solution1: Divide and Conquer
# To be continued

# Solution2: Backtracking
# Time: [Runtime: 1524 ms, faster than 18.30% of Python]
class Solution(object):
    def dfs(self, nums, path, stack, target):
        # print nums, path, stack
        if not nums:
            # print path, stack
            if sum(stack) == target:
                self.ans.append( "".join( path ) )
            return
        
        operation = ['+','-','*']
        
        for i in range(len(nums)):
            num = nums[:i+1]
            if num[0] == '0' and len(num) > 1:
                continue
            if not path:
                self.dfs(nums[i+1:], path + [num], [int(num)], target)
            else:
                for op in operation:
                    if op == '+':
                        self.dfs(nums[i+1:], path + [op, num], stack+[int(num)], target)  
                    elif op == '-':
                        self.dfs(nums[i+1:], path + [op, num], stack+[-int(num)], target)  
                    else:
                        self.dfs(nums[i+1:], path + [op, num], stack[:-1] + [stack[-1]*int(num)], target)  
                
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.ans = []
        
        self.dfs( num, [], [], target )
        
        return self.ans