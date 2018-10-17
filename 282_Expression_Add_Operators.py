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

class Solution(object):
    def dfs(self, num, path, prev_num, res, target, ans):
        if not num:
            if res == target:
                ans.append(path)
            return
        
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                curr_num = num[:i]
                self.dfs(num[i:], path + '+' + curr_num, int(curr_num), res + int(curr_num), target, ans )
                self.dfs(num[i:], path + '-' + curr_num, -int(curr_num), res - int(curr_num), target, ans )
                temp = prev_num * int(curr_num)
                self.dfs(num[i:], path + '*' + curr_num, temp, res - int(prev_num) + temp, target, ans )
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), target, ans)
        
        return ans