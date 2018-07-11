from collections import Counter

def findTheDifference(self, s, t):
	"""
	:type s: str
	:type t: str
	:rtype: str
	"""
	return "".join(list(Counter(t)-Counter(s)))