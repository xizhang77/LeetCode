def letterCasePermutation(S):
	"""
	:type S: str
	:rtype: List[str]
	"""
	if S.isdigit():
		return S
	else:
		S = S.lower()


print letterCasePermutation("12345")