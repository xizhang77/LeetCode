def letterCasePermutation(S):
	"""
	:type S: str
	:rtype: List[str]
	"""
	if S.isdigit():
		return S
	else:
		return 0


print letterCasePermutation("12345")