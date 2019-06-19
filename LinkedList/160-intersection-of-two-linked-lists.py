# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1
# Time: O(m+n); Space: O(n) or O(m)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stack = set()
        
        p = headA
        while p:
            stack.add( p )
            p = p.next
        
        
        q = headB
        while q and q not in stack:
            q = q.next
        
        return q


# Solution 2 [这个方法也适用于检查cycle，没事儿多想想…]
# Time: O(m+n); Space: O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        
        while p != q:
            if p:
                p = p.next
            else:
                p = headB
            
            if q:
                q = q.next
            else:
                q = headA
        
        return p