maxa=1
for i in range(1,1000):
	for j in range(1,1000):
		a=i*j
		convt=str(a)
		reverse=convt[::-1]
		int_convert=int(reverse)
		d=int_convert
		if a==d:
			if maxa<a:
				maxa=a
print(maxa)
