# -*- coding: utf-8 -*-

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = 0
        
        p, q = l1, l2
        
        while p and q:
            prev = p
            temp = p.val + q.val + res
            res = temp/10
            p.val = temp%10
            p = p.next
            q = q.next
        
        while p:
            prev = p
            temp = p.val + res
            res = temp/10
            p.val = temp%10
            p = p.next
                
        if q:
            prev.next = q
            while q:
                prev = q
                temp = q.val + res
                res = temp/10
                q.val = temp%10
                q = q.next
        
        if res:
            node = ListNode( res )
            prev.next = node
        
        return l1