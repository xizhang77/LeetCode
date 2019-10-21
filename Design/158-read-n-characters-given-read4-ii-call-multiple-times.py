# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
'''

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.stack = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count = n
        while len(self.stack) < n:
            buff = [""]*4
            length = read4( buff )
            self.stack += buff[:length]
            count -= length
            if count < 0 or length < 4:
                break
        
        ans = min( len(self.stack), n ) 

        buf[:ans] = self.stack[:ans]
        self.stack[:ans] = []
        
        return ans
        