# -*- coding: utf-8 -*-

'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''

# Time: O(rowIndex^2)
# Space: O(rowIndex)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        
        ans = [ 1, 1 ]
        
        for i in range(2, rowIndex + 1 ):
            temp = []
            for j in range( len(ans) - 1 ):
                temp.append( ans[j] + ans[j+1] )
            ans = [1] + temp + [1]
        
        return ans 