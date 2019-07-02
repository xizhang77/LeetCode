# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/linked-list-cycle/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n); Space: O(n)
class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = set()
        
        p = head
        
        while p:
            if p in stack:
                return True
            stack.add( p )
            p = p.next
        
        return False


# Time: O(n); Space: O(1)
# If cycle existed, the slow and fast pointer have to meet inside the cycle
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = q = head
        
        while p and p.next:
            p = p.next.next
            q = q.next
            if p == q:
                return True
        
        return False