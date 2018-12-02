#https://www.acmicpc.net/problem/1541
sik=list(input().split('-'))

t_num=0
for i, e in enumerate(sik):
	num=0
	d_sik=e.split('+')
	for j in d_sik:
		num+=int(j)	
	if(i!=0): t_num-=num
	else : t_num+=num

print(t_num)