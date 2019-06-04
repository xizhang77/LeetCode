# -*- coding: utf-8 -*-
'''
https://leetcode.com/problems/subdomain-visit-count/
'''

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        match = {}
        
        for item in cpdomains:
            count, domain = item.split(" ")
            domains = domain.split(".")
            for i in range( len(domains) ):
                d = ".".join( domains[i:] )
                if d not in match:
                    match[ d ] = int(count)
                else:
                    match[ d ] += int(count)
        
        return [ str(match[val]) + " " + val for val in match ]
        