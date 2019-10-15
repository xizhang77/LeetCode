# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/validate-ip-address/
'''


class Solution(object):
    def checkIPv4(self, nums):
        if len(nums) != 4:
            return 'Neither'
        
        for num in nums:
            if not num.isdigit() or (num[0] == '0' and len(num) > 1) or int(num) > 255:
                return 'Neither'
        
        return 'IPv4'
        
    def checkIPv6(self, nums):
        if len(nums) != 8:
            return 'Neither'
        
        hex_digits = set("0123456789abcdef")
        for num in nums:
            if not num or len(num) > 4 or (set(num.lower()) - hex_digits):
                return 'Neither'
        
        return 'IPv6'
        
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        if "." in IP:
            return self.checkIPv4( IP.split('.') )
        elif ":" in IP:
            return self.checkIPv6( IP.split(':') )
        else:
            return 'Neither'