# -*- coding: utf-8 -*-

'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

class Solution(object):
    def hundred(self, num):
        under20 = {0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        
        if num < 20:
            return [ under20[ num ] ]
        elif num < 100:
            return [ tens[ num/10 ], under20[ num%10 ] ]
        else:
            return [ under20[ num/100 ], "Hundred" ] + self.hundred( num%100 )
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        
        level = ["", "Thousand", "Million", "Billion"]
        
        ans = []
        for value in level:
            temp = []
            if num:
                temp += self.hundred( num%1000 ) 
                temp += [ value ] if num%1000 else []
                num = num/1000
                ans = temp + ans

        return " ".join( [val for val in ans if val != ''] )