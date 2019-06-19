# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/linked-list-cycle/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = set()
        
        p = head
        
        while p:
            if p in stack:
                return True
            stack.add( p )
            p = p.next
        
        return False