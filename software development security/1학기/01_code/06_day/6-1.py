# function that no return value
def func1(a):
	print(a*3)

print('start')
func1('agagd')

# function that return value
def sum(a,b):
	return a+b

a,b=input().split()
res=sum(int(a),int(b))
print(res)


# 함수는 선언하고 호출하는 위치가 중요하다
# c언어처럼 앞에서 프로토타입을 선언할 수 없을까? 아마 안 될거야
