def primenumber(number):
	for i in range(2,number):
		if number%i==0:
			pass
			return 1
			break
	else:
		return number
i=1	
j=1
while(i<10001):
	j=j+1
	a=primenumber(j)
	if a==1:
		pass
	else:
		i+=1
		print(a,"  ",i)	


	
