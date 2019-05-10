# -*- coding: utf-8 -*-

'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Time Complexity: O(N\log N)O(NlogN). 
Suppose our linked list consists of N elements. 
For every list we pass to our recursive function, 
we have to calculate the middle element for that list. 
For a list of size N, it takes N/2 steps to find the middle element 
i.e. O(N) to find the mid. We do this for every half of the original linked list.

However, on closer analysis, it turns out to be a bit more efficient than O(N^2).
After finding the middle element, we are left with two halves of size N/2 each. 
Then, we find the middle element for both of these halves and it would take a total of 2×N/4 steps for that. 
And similarly for the smaller sublists that keep forming recursively. 

Essentially, this is done NlogN times since we split the linked list in half every time. 
[Same as divide and conquer]

Space Complexity: O(\log N)O(logN). 
Since we are resorting to recursion, there is always the added space complexity 
of the recursion stack that comes into picture. This could have been O(N) for a skewed tree, 
but the question clearly states that we need to maintain the height balanced property. 
This ensures the height of the tree to be bounded by O(logN). 
Hence, the space complexity is O(logN).
'''
class Solution(object):
    def dfs(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode( head.val )
        
        # Find middle
        p = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        root = TreeNode( slow.val )
        
        root.left = self.dfs( head )
        root.right = self.dfs( slow.next )
        
        return root
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.dfs( head )

# This solution works for generating BST, not balanced BST

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        
        # Find middle
        p = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode( slow.val )
        
        # Generate right tree
        listp = slow.next
        treep = root
        while listp:
            treep.right = TreeNode(listp.val)
            treep = treep.right
            listp = listp.next
        
        # Generate left tree
        p, q = head, head.next
        while p != slow:
            qnext = q.next
            q.next = p
            if p.next == q:
                p.next = None
            p, q = q, qnext
        
        listp = slow.next
        treep = root
        while listp:
            treep.left = TreeNode(listp.val)
            treep = treep.left
            listp = listp.next
            
        return root