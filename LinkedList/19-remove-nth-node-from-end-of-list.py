# -*- coding: utf-8 -*-

'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n) 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode( None )
        temp.next = head
        
        prevq, q, p = temp, head, head
        count = 0
        
        while p:
            p = p.next
            count += 1
            if count > n:
                prevq = q
                q = q.next
        
        prevq.next = q.next
        
        return temp.next