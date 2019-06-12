# -*- coding: utf-8 -*-

'''
There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every third bulb 
(turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. 
For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
'''

# Solution 1 [LTE]
# Time: O(n^2)
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        ans = 1
        i = 2
        while i <= n:
            count, j = 1, 2
            while j < i:
                count = count + 1 if i%j == 0 else count
                j += 1
            ans = ans + (1-count%2)
            i += 1
        return ans


# Refer: https://blog.csdn.net/baidu_23318869/article/details/50386323
# 纯智力题？？？
class Solution2(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return int( n **0.5 ) 