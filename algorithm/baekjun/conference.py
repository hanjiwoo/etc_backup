from operator import itemgetter
# 끝나는 시간을 정렬하는 것이 팁
N= int(input())

Info=[]
min_end=0
max_conf=1

for i in range(N):
	start,end=map(int,input().split())
	Info.append([start,end])

Info.sort(key=itemgetter(1,0))
min_end=Info[0][1]

for i in range(1,len(Info)):
	if Info[i][0]>=min_end:
		min_end=Info[i][1]
		max_conf+=1

print(max_conf)
