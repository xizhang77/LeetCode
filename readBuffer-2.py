# -*- coding: utf-8 -*-

'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1: 

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""
Example 2: 

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""
'''

'''
解题思路：这道题和上一道题唯一不同的地方是，这一次read函数可以被调用多次。因此需要有一个全局变量来记录目前为止已经读了多少（而不是像上一道题，每次都从头开始）
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
	def __init__(self):
		self.queue = []

	def read(self, buf, n):
		"""
		:type buf: Destination buffer (List[str])
		:type n: Maximum number of characters to read (int)
		:rtype: The number of characters read (int)
		"""
		if not buff or n<=0:
			return 0

		idx = 0
		while 1:
			buff = ['']*4
			num = read4(buff)
			self.queue.extend(buff)
			temp = min( len(self.queue), n - idx)

			for i in range(temp):
				buf[idx] = self.queue.pop(0)
				idx += 1

			if idx == n or num < 4:
				return idx
