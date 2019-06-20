# -*- coding: utf-8 -*-

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1
# Time & Space: O(n)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val = []
        
        while head:
            val.append( head.val )
            head = head.next
        
        return val == val[::-1]


# Soluiton 2
# Time: O(n); Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        if slow == fast:
            if not slow or not slow.next:
                return True
            else:
                return slow.val == slow.next.val
            
        p = slow.next
        q = p.next
        slow.next = None
        
        while q:
            qnext = q.next
            q.next = p
            if p.next == q:
                p.next = None
            p = q
            q = qnext
        
        head2 = p
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        
        return True