# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
'''

# Time: O(klogk)
# Space: O(k)
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or not k:
            return []
        
        ans = []
        stack = []
        heapq.heappush( stack, ( nums1[0]+nums2[0], 0, 0 ) )
        
        
        while stack and len(ans) < k:
            _, i, j = heapq.heappop( stack )
            ans.append( [nums1[i],nums2[j]] )
            
            if j + 1 < len(nums2):
                heapq.heappush( stack, ( nums1[i]+nums2[j+1], i, j+1 ) )
            if j == 0 and i + 1 < len(nums1):
                heapq.heappush( stack, ( nums1[i+1]+nums2[0], i+1, 0 ) )
        
        return ans

# Time: O(klogk) (since we have break condition in the for loop)
# Space: O(k)
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        stack = []
        
        for i in nums1:
            for j in nums2:
                temp = i + j
                if len(stack) < k:
                    heapq.heappush( stack, (-temp, [i,j]) )
                else:
                    currmax = - stack[0][0]
                    if temp < currmax:
                        heapq.heappop( stack )
                        heapq.heappush( stack, (-temp, [i,j]) )
                    else:
                        break
        
        return[ val[1] for val in stack ]


# Time: O(m*n*log(k))
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        stack = []
        smin = None
        for i in nums1:
            for j in nums2:
                if smin == None or -(i+j) > smin:
                    heapq.heappush(stack, [ -(i+j), [i,j]] )
                if len(stack) > k:
                    val, idx = heapq.heappop( stack )
                    if smin == None:
                        smin = val
                    else:
                        smin = max( smin, val )

        return [ item[1] for item in stack ]