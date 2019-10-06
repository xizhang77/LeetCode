# -*- coding: utf-8 -*-

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


'''
# Solution 1: Priority Queue / Heap
# Time: O(k*n) (O(k) for sorting the heap)
# Space: O(k)
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        stack = []
        
        for num in nums:
            heapq.heappush( stack, num )
            if len(stack) > k:
                heapq.heappop( stack )
        
        return heapq.heappop( stack )

# Time: O(k*n) [faster than Solution 1]
class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        stack = []
        
        for num in nums:
            if len(stack) < k:
                heapq.heappush( stack, num )
            else:
                val = stack[0]
                if num > val:
                    heapq.heappop( stack )
                    heapq.heappush( stack, num )
        return stack[0]