# -*- coding: utf-8 -*-

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, 
only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n); Extra Space: O(1)
class Solution(object):
    def reverseList(self, head):
        if not head:
            return
        p = head
        q = p.next
        while q:
            nextq = q.next
            q.next = p
            if p.next == q:
                p.next = None
            p = q
            q = nextq
            
        return p
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        
        head2 = self.reverseList( head2 )
        
        p = head
        q = head2
        while q:
            nextp = p.next
            nextq = q.next
            p.next = q
            q.next = nextp
            
            p = nextp
            q = nextq
        
        
# Time and Space: O(n)
class Solution2(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        checklist = []
        
        p = head.next
        while p:
            checklist.append( p )
            p = p.next
        
        p = head
        i, j = 0, len(checklist) - 1
        flag = 1
        while i <= j:
            if flag:
                p.next = checklist[j]
                j -= 1
            else:
                p.next = checklist[i]
                i += 1
            p = p.next
            flag = 1 - flag
        p.next = None