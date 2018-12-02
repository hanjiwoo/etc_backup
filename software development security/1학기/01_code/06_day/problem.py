#str=input()

# while True:
# 	if str != 'quit':
# 		if str.find('skip') == -1:
# 			print('rejected')
# 		else : print(str)
# 		print('-'*10)
# 	else : break

# skip을 포함하는 문자열인 경우 rejected를 출력하고
# 구분선을 출력하지 않는 함수 
def print_without_skip(str):
	if 'skip' in str:
		print('rejected')
		return
	else:
		print(str)
	print('-'*10)

# quit을 입력할 때까지 반복하여 사용자 입력을 받음
user_input=' '
while user_input != 'quit':
	user_input = input('input: ')
	print_without_skip(user_input)