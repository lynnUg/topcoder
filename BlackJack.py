class TheBlackJackDivOne:
	def solve(self,s,C):
		#print s, C
		if s>=21:
			return 0
		total=0
		for i in range(2,12):
			total+=C[i]
		result=0
		#print total
		for i in range(2,12):
			if C[i]>0:
				C[i]-=1
				t=float(self.solve(s+i,C))
				C[i]+=1
				result+=t*C[i]
				print i,result
		return float(result)/float(total+1.0)
	def expected(self,cards):
		C={}
		for i in range(2,10):
			C[i]=4
		C[10]=16
		C[11]=4
		s=0
		for card in cards:
			c=card[0]
			d=0
			if c=='T' or c=='J' or c=='Q' or c=='K':
				d=10
			elif c=='A':
				d=11
			else:
				d=int(c)
			C[d]-=1
			s+=d
		print s, C
		ret=self.solve(s,C)
		return ret
test=TheBlackJackDivOne()
print test.expected(["JS"])