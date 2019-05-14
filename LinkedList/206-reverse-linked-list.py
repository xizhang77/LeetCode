# -*- coding: utf-8 -*-

'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1: Iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        p, q = head, head.next
        
        while q:
            qnext = q.next
            q.next = p
            if p.next == q:
                p.next = None
            p, q = q, qnext
        
        return p

# Solution 2: Recursively
class Solution(object):
    def dfs(self, node):
        if not node or not node.next:
            return node, node
        
        head, tail = self.dfs( node.next )
        tail.next = node
        
        return head, node
        
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head, new_tail = self.dfs( head )

        # Only used to avoid empty input
        if new_tail:
            new_tail.next = None
        
        return new_head