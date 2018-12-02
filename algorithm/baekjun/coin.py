N=0
K=0
coin=[]
coin_i=0
g=0

N,K=input().split()
N=int(N)
K=int(K)

for i in range(0,N):
	a=int(input())
	coin.append(a)
	if coin[i]<K : coin_i=i # 입력한 값 보다 작은(즉 작은 것들 중 최대값 찾음) 수의 인덱스

for i in range(coin_i,0,-1): # 입력한 값보다 작은 수의 인덱스부터 역순으로(-1)
	if K>0:
		g+=K//coin[i] # 몫 연산(= 사용된 동전 개수)
		K=K%coin[i] # 나머지

print(g)
