# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/unique-morse-code-words/
'''

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hashMap = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        
        check = set()
        
        for word in words:
            morse = "".join( [hashMap[c] for c in word] )
            check.add( morse )
        
        return len(check)