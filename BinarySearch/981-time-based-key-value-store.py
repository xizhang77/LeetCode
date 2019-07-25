# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/time-based-key-value-store/
'''

from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = defaultdict(list)
        self.v = defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.t[ key ].append( timestamp )
        self.v[ key ].append( value )
    
    def binarySearch(self, nums, target):
        i, j = 0, len(nums)-1
        while i <= j:
            mid = i + (j-i)/2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1
        
        return j
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if timestamp < self.t[key][0]:
            return ""
        if timestamp >= self.t[key][-1]:
            return self.v[key][-1]
        
        idx = self.binarySearch( self.t[key], timestamp )
        return self.v[key][idx]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)