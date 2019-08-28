# -*- coding: utf-8 -*-

'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

'''

# Time: O(nlogk); Space: O(k)
import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        stack = []
        
        currmax = - float('inf')
        
        for num in arr:
            diff = abs(num-x)
            if len( stack ) < k:
                heapq.heappush( stack, (- diff, num) )
                currmax = max( currmax, diff )
            else:
                temp = heapq.heappop( stack )
                if diff < - temp[0]:
                    heapq.heappush( stack, (- diff, num) )
                    currmax = min( currmax, -temp[0] )
                else:
                    heapq.heappush( stack, temp )
            # print currmax, diff, num
            if currmax < diff and len(stack) == k:
                break
        
        return sorted([ val[1] for val in stack])


# Brute-Force to find minimum
# Time: O(n); Space: O(1)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        currmin = float('inf')
        idx = 0
        while i < len(arr):
            if abs(arr[i] - x) > currmin:
                break
            else:
                currmin = abs(arr[i] - x)
                idx = i
            i += 1
        
        if idx == 0:
            return arr[:k]
        elif idx == len(arr) - 1:
            return arr[-k:]
        
        p = q = idx 
            
        while p >= 0 and q < len(arr) and q - p + 1 < k:            
            if p == 0:
                q += 1
            elif q == len( arr ) - 1:
                p -= 1
            else:
                if abs(arr[p-1] - x) <= abs(arr[q+1] - x):
                    p -= 1
                else:
                    q += 1
            
        return arr[p:q+1]

# Binary Search to find minimum
# To be continued