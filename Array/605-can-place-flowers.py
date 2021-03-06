# -*- coding: utf-8 -*-

'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''

# Time: O(len(flowerbed)); Space: O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed) and flowerbed[i] == 0:
            i += 1
        if i == len(flowerbed):
            return (len(flowerbed)+1)/2 >= n
        n -= i/2
        
        j = len(flowerbed) - 1
        while j >= 0 and flowerbed[j] == 0:
            j -= 1
        n -= (len(flowerbed) - 1 - j)/2
        
        # print i,j,n
        if n <= 0:
            return True
                
        p = i + 1
        count = 0
        while p <= j:
            if flowerbed[p] == 0:
                count += 1
            else:
                n -= (count-1)/2
                count = 0
            p += 1
            
        return n <= 0