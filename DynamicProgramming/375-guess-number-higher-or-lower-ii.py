# -*- coding: utf-8 -*-

'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. 
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''

'''
这道题其实是比较经典的2D DP问题，但是题目写的非常晦涩……
总之，题目希望得到最少花销，既对于每一个初始num，求它能达到的最坏情况，最终选择cost最小的一条。（minmax问题）

Refer: https://blog.csdn.net/fuxuemingzhu/article/details/82893656
'''

# Solution 1: Recursive DP
# Time: O(n^3); Space: O(n^2)
class Solution(object):
    def solver(self, dp, l, r):
        if l >= r:
            return 0
        if dp[l][r]:
            return dp[l][r]
        
        dp[l][r] = min(i + max(self.solver(dp, l, i-1), self.solver(dp, i+1, r)) for i in range(l, r+1))
        return dp[l][r]
    
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [ [0] *(n+1) for _ in range(n+1) ]
        
        return self.solver(dp, 1, n)