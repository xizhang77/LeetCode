# -*- coding: utf-8 -*-

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1
# Time: O(kn) [Runtime: 5356 ms, faster than 6.82%]
class Solution(object):
    def remove(self, lists):
        n = len(lists)
        i = 0
        while i < n:
            if not lists[i]:
                lists.pop(i)
                n -= 1
            else:
                i += 1
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.remove( lists )
        
        if not lists:
            return None  
        
        head = ListNode( None )
        p = head 
        
        while lists:
            temp, idx = lists[0], 0
            for i, node in enumerate(lists):
                if node and node.val < temp.val:
                    temp, idx = node, i
                elif not node:
                    node.pop( i )
            p.next = temp
            p = p.next
            
            if temp.next:
                lists[ idx ] = temp.next
            else:
                lists.pop( idx )
                    
        return head.next


# Solution 2: Heap [Runtime: 96 ms, faster than 67.50%]
# Time: O(Nlogk) [O(logk) for heappop] 
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        stack = []
        
        for node in lists:
            if node:
                heapq.heappush( stack, [ node.val, node ])
        
        head = ListNode( None )
        p = head
        while stack:
            val, node = heapq.heappop( stack )
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush( stack, [ node.next.val, node.next ])
        
        return head.next