N,M,K=map(int, input().split())

i=0
team=0 
tmp=0

for i in range(0,K+1):
	Nn=(N-i)//2
	Mm=M-(K-i)

	if N>0 and M>0:
		tmp = Nn if Nn<=Mm else Mm
		
		if tmp > team :
			team = tmp
	else : continue

print(team)



