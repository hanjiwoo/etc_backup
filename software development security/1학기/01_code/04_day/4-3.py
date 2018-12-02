# i=0
# while i<3:
# 	print(i)
# 	i=i+1

while True:
	a=input("숫자나 문자를 입력하시오 : ")
	if a=='1' and int(a)==1: #문자(열)을 숫자로 바꾸고 숫자와 비교하는 것이 사실 불가능 
		print("The end")
		break
	else :
		print("This is not one")