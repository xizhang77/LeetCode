# -*- coding: utf-8 -*-

'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Example 1:
Input: buf = "abc", n = 4
Output: "abc"
Explanation: The actual number of characters read is 3, which is "abc".

Example 2:
Input: buf = "abcde", n = 5 
Output: "abcde"

Note:
The read function will only be called once for each test case.
'''

'''
这道题的大致理解：模拟内存从硬盘中读数据的方法，先从硬盘读一整块数据到缓冲区，之后内存根据需求从缓冲区request。
提供的functions：
	Read4: 从硬盘读数据到内存区。硬盘的情况通过Read4的API隐式表达
	Read: 体现实际的内存读数据需求

read4每调用一次，都会向内存输出4个字符（并且填入buf相应的位置），并返回此次调用返回数据的长度（<=4）。

在这道题中，硬盘数据是隐藏的，并不存在于buf中，而是需要我们调用read4的API得到，并且将得到的数据存入buf（可以将buf当做头指针，直接modify即可，不需要return）。
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
	def read(self, buf, n):
		"""
		:type buf: Destination buffer (List[str])
		:type n: Maximum number of characters to read (int)
		:rtype: The number of characters read (int)
		"""

		if not buf or n <= 0:
			return 0

		ans = 0
		idx = 0
		buff = ['']*4

		while 1:
			num = read4(buff)
			ans += num
			for i in range(num):
				buf[idx] = buff[i]
				idx += 1

			if num < 4 or idx >= n:
				return min(ans, n)
				break
