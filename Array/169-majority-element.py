# -*- coding: utf-8 -*-

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

# Time: O(nlogn) due to the sorting fuction
# One can also use a hash table to accelerate (time: O(n); Space: O(n))
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[ len(nums)/2 ]


# Solution 2 [题目真正想考的解题方法：最大投票原理]
# Time: O(n); Space: O(1)
'''
因为数组个数为n，且最多数元素个数>⌊ n/2 ⌋，则有且只有1个元素满足条件，所以设置了一个candidate和一个计票器count。

遍历数组,当碰到两个不一样的数字时,将这两个数字同时丢弃，这两个数字中可能有一个为 Majority Element,
也可能两个都不是.因为 count 大于 n/2,所以在最差情况下(每次移除不同数字时都包含一个Majority Element),
我们仍然能够保证最后得到的数字是Majority Element.
总之：在原序列中去除两个不同的元素后，在原序列中的多数元素在新序列中还是多数元素。       
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        
        ans = count = 0
        
        
        for num in nums:
            if count == 0:
                ans, count = num, 1
                continue
                
            if num == ans:
                count += 1
            else:
                count -= 1
        
        return ans 