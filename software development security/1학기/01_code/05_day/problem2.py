'''
현재 상태 : 암호코드가 입력된 상황
목표 상태 : 암호코드에서 암호문의 문자를 찾아 인덱스 출력
핵심요소1 : 공백이 입력되면 공백을 반환
핵심요소2 : 믄자가 입력되면 암호문을 순차 탐색하여 인덱스 반환
'''

# 내가 짠 코드 # 인덱스 값 오류가 있었음 # encode 문자열의 크기로 잡아줘야함(9를 넘어갈 수 있기 때문에)
# code=input("코드표를 입력하시오 : ")
# encode=input("암호문을 입력하시오 : ")
# decode=''

# for i in range(0,len(encode)):
# 	if encode[i]==' ': decode=decode+' '
# 	else: decode=decode+str(code.find(encode[i]))

# print(decode)

# 최종 정답
a=input("코드표를 입력하시오 : ")
b=input("암호문을 입력하시오 : ")

#1
# while(i<len(b)):
# 	if b[i]!=' ':
# 		print(a.find(b[i]),end="")
# 	else: 
# 		print(b[i],end="")
# 	i=i+1 

#2
#while(i<len(b)):
#	print(a.find(b[i]) if b[i]!=' ' else b[i], end="")
#	i=i+1

#3
for i in b:
	print(a.find(i) if i!=' ' else i, end="")

