lis=[]
count=0
temp1=1
temp2=2
lis=[temp1,temp2]
fib=0
while(fib<4000000):
	fib=temp1+temp2
	temp1=fib-temp1
	temp2=fib
	lis.append(fib)
lis2=[]
for i in lis:
	if i%2==0:
		lis2.append(i)
temp=0
for i in lis2:
	sum1=temp+i
	temp=sum1
print(sum1)	