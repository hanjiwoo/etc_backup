import random
alist=["*"]
for i in range(1,31):
	alist.append(i)
for i in range(11,21):
	alist.append(i)
random.shuffle(alist)

print("숫자를 무작위로 고르시오")
for i in range(1,21):
	input()
	print(i,"번째 숫자: ",alist[i]) 
	print("\n"*20)

