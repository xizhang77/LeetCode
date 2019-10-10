# -*- coding: utf-8 -*-

'''
Given a non-negative integer represented as non-empty a 
singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, 
except the number 0 itself.

The digits are stored such that the most significant digit is 
at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time and Space: O(n)
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return ListNode( 1 )
        
        stack = []
        p = head
        
        while p:
            stack.append( (p.val, p))
            p = p.next
        
        res = 1
        while res and stack:
            num, node = stack.pop()
            newnum = ( num + res )%10
            res = ( num + res )/10
            
            node.val = newnum
        
        if not stack and res:
            node = ListNode( 1 )
            node.next = head
            return node
        
        return head