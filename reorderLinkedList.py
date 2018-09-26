# -*- coding: utf-8 -*-

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

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

class Solution(object):
	def reorderList(self, head):
		"""
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		"""
		while head and head.next and head.next.next:
			fast, slow = head, head
			while fast.next and fast.next.next:
				fast = fast.next.next
				slow = slow.next

			head1, head2 = head, slow.next
			slow.next = None

			#Reverse the 2nd half
			q = head2.next
			head2.next = None
			while q:
				temp = q.next
				q.next = head2
				head2 = q
				q = temp

			p, q = head1, head2
			while q:
				pnext = p.next
				qnext = q.next
				p.next = q
				q.next = pnext
				p, q = pnext, qnext