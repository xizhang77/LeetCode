# -*- coding: utf-8 -*-

'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, head1, head2):
        head = ListNode(None)
        p = head
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        
        if head2:
            p.next = head2
        
        if head1:
            p.next = head1
        
        return head.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        
        return self.merge( self.sortList(head), self.sortList(head2) )