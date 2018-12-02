# 1
# a,b=input().split()
# print(a.replace('',b))

# 2
# a=[]
# a.append(input().split())

# 3
a,b=map(int,input().split())
min= a if a<b else b
c=[]
for i in range(2,min+1):
	c.append(i) if a%i==0 and b%i==0 else None
print(c)

''' before 과정
a,b=input().split() 
a=int(a)
b=int(b)
--------------------
a,b=map(int,input().split())
min=0
if a<b : min = a
else : min = b
--------------------
a,b=map(int,input().split())
min= a if a<b else b
c=[]
for i in range(2,min+1):
	if a%i==0 and b%i==0 : c.append(i)
	else None
print(c)
---------------------
a,b=map(int,input().split())
min= a if a<b else b
c=[]
for i in range(2,min+1):
	c.append(i) if a%i==0 and b%i==0 else None
print(c)
'''