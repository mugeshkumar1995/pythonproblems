def primefactor(number):
	def primenumber(number):
		for i in range(2,number):
			if number%i==0:
				pass
				break
		else:
			return number
	lis=[]
	for i in range(2,number):
		lis.append(primenumber(i))
	lis1=set(lis)
	lis1.remove(None)
	list2=[]
	for i in lis1:
	 	if number%i==0:
	 		list2.append(i)
	print(list2[-1]) 		

primefactor(600851475143)				