N=0
max_n=[]
sum_n=0
min_n=[]
r_min=0 # 음수 배열에서 개수가 홀수일때 마지막에 남는 숫자
flag=0

N=int(input())

for i in range(0,N):
	a=int(input())
	if a<0 :
		min_n.append(a)
	else :
		max_n.append(a)

min_n.sort()
max_n.sort()

# 음수 배열 
# 짝수 개일 때
if len(min_n)%2==0:
	for i in range(0,len(min_n),2):
		sum_n+=(min_n[i]*min_n[i+1])
# 홀수 개일 때
else :
	# 마지막에 남는 것 r_min에 넣어주기 # 0 있을 때 곱해주기 위해
	r_min=min_n[len(min_n)-1] 
	for i in range(0,len(min_n)-1,2):
		sum_n+=(min_n[i]*min_n[i+1])

# 양수 배열
# 짝수 개일 때
if len(max_n)%2==0:
	for i in range(0,len(max_n),2):
		if max_n[i]==1: sum_n+=max_n[i]+max_n[i+1]
		elif max_n[i]==0 :
			if flag==0:
				sum_n+=(max_n[i]*r_min)+max_n[i+1]
				flag=1
			else :
				sum_n+=max_n[i]+max_n[i+1]
		else :
			sum_n+=max_n[i]*max_n[i+1]
# 홀수 개일 때
else:
	# 가장 작은 값이 0일때 음수 배열에서 
	if max_n[0]==0:
		sum_n+=(max_n[0]*r_min)
		flag=1
	else : 
		sum_n+=max_n[0]
	for i in range(len(max_n)-2,0,-2):
		if max_n[i]==1: sum_n+=max_n[i]+max_n[i+1]
		elif max_n[i]==0 :
			if flag==0:
				sum_n+=(max_n[i]*r_min)+max_n[i+1]
				flag=1
			else :
				sum_n+=max_n[i]+max_n[i+1]
		else :
			sum_n+=max_n[i]*max_n[i+1]

if flag!=1 :
	sum_n+=r_min

# if N%2==0:
# 	for i in range(0,N,2):
# 		if num[i]*num[i+1] > 0:
# 			sum_n+=(num[i]*num[i+1])
# 		else:
# 			sum_n += (num[i]+num[i+1])

print(sum_n)