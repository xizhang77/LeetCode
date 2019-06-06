# -*- coding: utf-8 -*-

'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

'''

# Solution 1: Priority Queue / Heap
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 
        stack, check = [], set()
        count = 0
        i = j = 0
        while count < k:
            if not stack:
                heapq.heappush(stack,  (matrix[0][0], (0,0)) )
                check.add( (0,0) )
                continue
            val, idx = heapq.heappop( stack )
            i, j = idx
            if i + 1 < len(matrix) and (i+1, j) not in check:
                heapq.heappush(stack,  (matrix[i+1][j], (i+1, j)) )
                check.add( (i+1, j) )
            if j + 1 < len( matrix ) and (i, j+1) not in check:
                heapq.heappush(stack,  (matrix[i][j+1], (i, j+1)) )
                check.add( (i, j+1) )
            
            count += 1
        
        return val


# Solution 2: Binary Search
# Refer: http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/
class Solution(object):
    def countSmallest(self, matrix, val):
        i, j = len(matrix) -1, 0 
        count = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] > val:
                i -= 1
            else:
                count += i + 1
                j += 1
        return count
    
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        i, j = matrix[0][0], matrix[-1][-1]
        
        while i <= j:
            mid = (i+j)/2
            cnt = self.countSmallest( matrix, mid )
            if cnt < k:
                i = mid + 1
            else:
                j = mid - 1
        
        return i