# -*- coding: utf-8 -*-

'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
'''


'''
一道脑筋急转弯…
如果石头是四的倍数的时候谁先拿x个，另一个就可以拿4-x个，这样到最后剩下4个的时候先拿的就会输掉，
所以只要自己先拿，让石头个数变为4的倍数，就可以让对方输掉，所以只要验证个数是不是4的倍数就可以了。
1，Y 
2，Y 
3，Y 
4，N 
5，Y 
6，Y 
7，Y 
8，N 
9，Y 
......

'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0