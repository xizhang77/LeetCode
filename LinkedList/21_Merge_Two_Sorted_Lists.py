# -*- coding: utf-8 -*-
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time: O(max(n1, n2)); Space: O(1)
class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        
        if l1.val > l2.val:
            l1, l2 = l2, l1
        
        p, q = l1, l2
        while p and q and p.next:
            pnext, qnext = p.next, q.next
            if p.val <= q.val <= p.next.val:
                p.next = q
                q.next = pnext
                p = q
                q = qnext
            else:
                p = pnext
        
        if q:
            p.next = q
        
        return l1


# Solution 2: much more clear

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = temp = ListNode(None)
        
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        head.next = l1 or l2
        
        return temp.next