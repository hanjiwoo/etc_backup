#https://www.acmicpc.net/problem/1780
zero=0
one=0
minus=0

def same(paper,s,e,N):
	for i in range(s,s+N):
		for j in range(e,e+N):
			if paper[i][j]!=paper[i][j+1]:
				return False
	return True

def check(paper,s,e,N):
	if(same(paper,s,e,N)):
		
	else:
		N/=3


N=int(input())

paper=[]

for i in range(N):
	paper.append(map(int,input().split()))

check(paper,0,0,N)

