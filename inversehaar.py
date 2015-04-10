class InverseHarr:
	def transform(self,data, L):
		if L>1:
			data2,data3=[],[]
			for i in range(0, len(data)/2):
				data2.append(data[i])
			data3=self.transform(data2,L-1)
			for i in range(0,len(data/2)):
				data[i]=data3[i]
		
		i,leng=len(data),len(data)
		res=[None for i in range(0,leng)]
		for i in range (0,leng/2):
			res[i*2]=(data[i]+data[leng/2+i])/2
			res[i*2+1]=(data[i]-data[leng/2+i])/2
		return res
test=InverseHarr()
print test.transform([101, -53],1)


