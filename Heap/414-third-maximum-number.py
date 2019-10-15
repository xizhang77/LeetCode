# -*- coding: utf-8 -*-

'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = set()
        heap = []
        
        for num in nums:
            if num in check:
                continue
            check.add( num )
            
            if len(heap) < 3:
                heapq.heappush( heap, num )
            else:
                # print heap[-1], heap[0]
                if num > heap[0]:
                    heapq.heappop( heap )
                    heapq.heappush( heap, num )

        if len(heap) == 3:
            return heap[0]
        else:
            return heap[-1]