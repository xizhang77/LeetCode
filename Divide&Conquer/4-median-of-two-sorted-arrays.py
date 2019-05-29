# -*- coding: utf-8 -*-

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

'''
Refer: https://www.cnblogs.com/zuoyuan/p/3759682.html

这道题目要求O(log(m+n))的时间复杂度，所以考察的是二分查找/分治法。

首先我们来看如何找到两个数列的第k小个数，即程序中 findKth(A, B, k)函数的实现。
用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；
如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；
k/2 = 7/2 = 3，而A中的第3个数A[2]=5；B中的第4个数B[2]=8；
而A[2]<B[3]；则A[0]，A[1]，A[2]中必然不可能有第7个小的数。

因此我们要求的getKth(A, B, 7) 就变成了 getKth(A', B, 4)；即A' = {7}；B不变，求这两个数列的第4个小的数，
因为A[0]，A[1]，A[2]中没有解，所以直接删除。
'''
class Solution(object):
    def findKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findKth( nums2, nums1, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min( nums1[0], nums2[0] )
        
        idx1 = min( k/2, m )
        idx2 = k - idx1
        
        if nums1[ idx1 - 1 ] <= nums2[ idx2 - 1 ]:
            return self.findKth( nums1[idx1:], nums2, k - idx1 )
        else:
            return self.findKth( nums1, nums2[idx2:], k - idx2 )
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        
        if (m + n)%2 == 0:
            return float( self.findKth( nums1, nums2, (m+n)/2 ) + self.findKth( nums1, nums2, (m+n)/2+1 ) ) / 2
        else:
            return float( self.findKth( nums1, nums2, (m+n)/2 + 1 ) )