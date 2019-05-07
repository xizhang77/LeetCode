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

class Solution(object):
	def reverseList(self, head):
		"""

		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return None
		prevp = None
		currp = head
		nextp = curr.next
		while nextp:
			prevp = currp
			currp = nextp
			nextp = nextp.next 
			currp.next = prevp
			if prevp.next == currp :
				prevp.next = None

		return currp