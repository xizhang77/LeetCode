# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/reorder-log-files/
'''

from operator import itemgetter
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit = []
        
        for log in logs:
            log = log.split(" ")
            logid, content = log[0], " ".join(log[1:])
            if content[0].isdigit():
                digit.append( logid + " " + content )
            else:
                letter.append( (logid, content) )
        
        temp = sorted(letter, key=itemgetter(1,0), reverse = False )
        return [ item[0] + " " + item[1] for item in temp ] + digit