def stair(s_num):
	'''
	if s_num==1 : return 1
	elif s_num==2 : return 2
	줄일 수 있음
	'''
	if s_num<3:return s_num
	else : return stair(s_num-1)+stair(s_num-2)
 
s_num = int(input("계단의 개수를 입력하시오 : "))
print(stair(s_num))