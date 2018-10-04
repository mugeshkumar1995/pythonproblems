def primenumber(number):
	for i in range(2,number):
		if number%i==0:
			pass
			break

	else:
		return number
def primefactor(number):
	for i in range(2,number):
		a=primenumber(i)
		if a==None:
			pass
		else:
			if number%a==0:
				print(a)	

primefactor(600851475143)				