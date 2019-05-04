# -*- coding: utf-8 -*-

'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''
'''
注释：用暴力求解如果调用sumRegion的次数太多，则会LTE。所以预先计算出所有[i,j]到[0,0]的所有元素的和，
    之后就可以用计算矩形重叠面积的方法来计算出想要的结果。
'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.table = [ [0 for i in range(n+1)] for j in range(m+1) ]
        
        for i in range(1, m+1):
            if i == 1:
                self.table[i][1] = matrix[i-1][0]
            else:
                self.table[i][1] = self.table[i-1][1] + matrix[i-1][0]
            for j in range(2, n+1):
                if i == 1:
                    self.table[i][j] = self.table[i][j-1] + matrix[i-1][j-1]
                else:
                    self.table[i][j] = self.table[i][j-1] + self.table[i-1][j] + matrix[i-1][j-1] - self.table[i-1][j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.table[row2+1][col2+1] - self.table[row2+1][col1] - self.table[row1][col2+1] + self.table[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)