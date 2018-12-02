'''
def hanoi(h_num):
	if h_num==1: return 1 #유한성, 조건
	else : return hanoi(h_num-1)+1+hanoi(h_num-1) #입력 0개 이상, 출력 1개 이상

h_num = int(input("하노이 원판의 개수를 입력하시오 : "))
print(hanoi(h_num))
'''
#간단히
h_num = int(input("하노이 원판의 개수를 입력하시오 : "))
print(2**h_num-1)
# 문제 분해를 통해 구조를 알아낸 후 이를 수학적으로 구현한다.
