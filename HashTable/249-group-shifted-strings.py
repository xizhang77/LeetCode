# -*- coding: utf-8 -*-

'''
Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, 
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        
        check = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l': 12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
        
        hashmap = {}
        
        for string in strings:
            flag = 1
            for key in hashmap:
                if len(key) == len(string):
                    mark = 1
                    temp = (check[key[0]]-check[string[0]] + 26)%26
                    for i in range( 1, len(key) ):
                        if temp != (check[key[i]]-check[string[i]] + 26)%26:
                            mark = 0
                            break
                    if mark:
                        flag = 0
                        hashmap[ key ] += [ string ]
            if flag:
                hashmap[ string ] = [ string ]
        
        
        return [val for val in hashmap.values()]