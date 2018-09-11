import collections
def customSortString(S, T):
	"""
	:type S: str
	:type T: str
	:rtype: str
	"""
	result = ""

	diffS = "".join(str(i) for i in (set(S) - set(T)))
	for char in diffS:
		S  = S.replace(char, "")

	countT = collections.Counter(T)
	for char in S:
		print char
		result = result + char*countT[char]
		T = T.replace(char, "")

	return result + T



print customSortString("ctax", "aabcdd")

