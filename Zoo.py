
class Zoo:
	def count (self,answers):
		cummulative={}
		themax=0
		ans=1
		y=False
		for answer in answers:
			if answer in cummulative:
				cummulative[answer]+=1
			else:
				cummulative[answer]=1
			themax=max(themax,answer)
		for item in cummulative:
			if cummulative[item]>2 or cummulative==0:
				return 0
		j=0
		for item in cummulative:
			if cummulative[item]!=2:
				break
			j+=1
		if j==0:
			y=True
		for i in range(j,themax):
			if cummulative[i]==2:
				return 0
		for item in cummulative:
			ans*=cummulative[item]
		if y or cummulative[themax]==1 and cummulative[0]==2:
			ans*=2
		return ans
test=Zoo()
print test.count([0,1,2,3,4])
print test.count([1, 0, 2, 0, 1])



