N = list(map(int,input()))

N.sort(reverse=True)

Sum=0
Max = ""

for i in range(0,len(N)):
	Sum+=N[i]
	Max+=str(N[i])
		
if Sum % 3 == 0 and N[len(N)-1]==0:
	print(int(Max))

else : print(-1)