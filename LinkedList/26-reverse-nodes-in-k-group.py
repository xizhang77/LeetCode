# -*- coding: utf-8 -*-

'''
Given a linked list, reverse the nodes of a linked list k at a time 
and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(2*n)= O(n); Space: O(1)
class Solution(object):
    def reverse(self, root):
        p = root
        q = root.next
        while q:
            nq = q.next
            q.next = p
            if p.next == q:
                p.next = None
            p = q
            q = nq
        
        return p, root
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or not head:
            return head
        
        root = ListNode(None)    
        root.next = head
        
        end = root
        p = head
        while True:
            start = p
            count = 1
            while p and p.next and count < k:
                p = p.next
                count += 1
            
            if count < k:
                break
            nextp = p.next
            p.next = None
            
            new_head, new_tail = self.reverse( start )
            end.next = new_head
            new_tail.next = nextp
            end = new_tail
            p = nextp
                
        
        return root.next