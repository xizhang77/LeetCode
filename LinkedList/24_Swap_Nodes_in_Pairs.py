# -*- coding: utf-8 -*-
'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n/2); Space: O(1)
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = temp = ListNode( None )
        
        p.next = head
        
        while p and p.next and p.next.next:
            i, j, k = p.next, p.next.next, p.next.next.next
            p.next = j
            j.next = i
            i.next = k
            p = p.next.next
        
        return temp.next