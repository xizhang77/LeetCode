# -*- coding: utf-8 -*-

'''
不LTE的修改方式：在Union function中，将weight小的树和weight大的树合并，这样就可以尽量保持树的平衡，降低层数
'''
class Solution(object):
	def __init__(self):
		self.parent = {} # main union-find data structure

	def Find(self, mail ):
		weight = 0
		while self.parent[ mail ] != mail:
			weight += 1
			mail = self.parent[ mail ]

		return weight, mail

	def Union(self, mail1, mail2 ):
		weight1, parent1 = self.Find( mail1 )
		weight2, parent2 = self.Find( mail2 )

		if weight1 <= weight2:
			self.parent[ parent1 ] = parent2
		else:
			self.parent[ parent2 ] = parent1

	def accountsMerge(self, accounts):
		"""
		:type accounts: List[List[str]]
		:rtype: List[List[str]]
		"""
		ans = []
		if not accounts:
			return ans

		owner = {} # store the email-name relationship (key: email; value: name)
		emailset = set()
		for account in accounts:
			name, emails = account[0], account[1:]
			for email in emails:
				emailset.add( email )
				owner[ email ] = name
				if email not in self.parent:
					self.parent[ email ] = email
			for email in emails[1: ]:
				self.Union( emails[0], email )

		unionset = {}
		for email in emailset:
			parent = self.Find(email)[1]
			if parent not in unionset:
				unionset[ parent ] = [ ]
			unionset[ parent ].append( email )
		print unionset
		for email in unionset.keys():
			ans.append([owner[email]] + sorted(unionset[email]) )

		return ans

obj = Solution()
# print obj.accountsMerge( [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]] )

print obj.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])