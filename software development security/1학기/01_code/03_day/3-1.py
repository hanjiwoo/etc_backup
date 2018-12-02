# 문자열 함수 

# count
a = 'programming'
res = a.count('m')
print(res)
# count 함수가 메소드로 지정된 변수의 문자열에서
# count 함수 인자(문자)의 개수를 반환한다.
# 만약 a에 숫자를 담고 count에 숫자 인자를 넣으면?
# -> 불가능하다. 이유는 문자열 함수이기 때문
# -> 그래도 숫자를 세고 싶다면?

# find
a = 'programming'
res = a.find('m')
print(res)
# find 함수가 메소드로 지정된 변수의 문자열에서
# find 함수 인자(문자)의 인덱스를 반환한다.
# 만약 찾는 문자가 없다면? => -1 출력
# 반환되는 -1이 정수이기 때문에 연산이 가능하다.
# ex) if(res==-1) 또는 res+1

# index
a = 'programming'
res = a.index('m')
print(res)
# 만약 찾는 문자가 없다면? => 에러 출력

# join
a = '_m-_-m_'
res = a.join('ABC')
print(res)
# join 함수가 메소드로 지정되 변수의 문자를
# join 함수의 인자(문자)사이에 삽입한다.
# 숫자도 될까? => 당연히 안 됨. 문자열 함수이므로.
# 가능하게 하는 방법은? => 숫자를 문자로 지정해주면 가능
# 한 줄씩 띄우게 하고 싶을 땐?
# => a='\n'

# 타임
a = [1,'sfsdfsd',123,'ssdfs']
print(str(a[1:4])[1:-1])
print(str(a)[1:-1]) #대괄호를 뺀 결과 (꼼수)

# upper
a = 'programming'
res = a.upper()
print(res)
# 대문자로 변환한 값을 반환한다.

# lower
a = 'PROGRAMMING'
res = a.lower()
print(res)
# 소문자로 변환한 값을 변환한다.
# '특수'문자에 대해서도 될까? => upper, lower 둘 다 안됨.

# replace
a = 'programmer'
res = a.replace('','1')
print(res)
# 문자열을 치환한 결과를 반환한다.
# 공백으로부터 치환이 가능할까? replace('','1')
# 공백으로 치환이 가능할까? replace('g','')
# 띄어쓰기로부터 치환이 가능할까? replace(' ','1')
# 없는 문자열은 치환이 불가능하다. => 원본 그대로 출력

# split
a = 'a1p1p1l1e'
res = a.split('1')
print(res[0]+res[1]+res[2]+res[3]+res[4])
# 문자열을 나눈 결과를 반환한다. => result is list type
# a = 'a1p1p1l1e' // res =a.split('1')
# 결과가 리스트이므로 나눈 결과를 결합하려면 인덱스를 활용한다.

# lstrip
a = '      programming       '
res = a.lstrip()
print(res)
print(res+'1') # 왼쪽 공백만 제거되었는지 확인

# rstrip
a = '      programming       '
res = a.rstrip()
print(res)
print(res+'1') # 오른쪽 공백만 제거되었는지 확인

# strip
a = '      programming       '
res = a.strip()
print(res)
print('1'+res+'1') 

# type
a = 'programming'
res = type(a)
print(res)
# res에 type 함수의 반환값을 넣을 수 있을까?
# 반환값이 있기 때문에 인자에 넣고 출력할 수 있음
# 반환값이 없는 함수 결과값을 인자에 넣고 출력하면 none 이 뜸 

# str
a = 123
res = str(a)
print(res*10)
# 숫자를 문자열로 바꿈
# 문자열인지 판단하는 방법 => *10
# 문자를 문자열로 바꾸는 것은 ? => 당연히 가능

# int
a = '123'
res = int(a)   # 실수로 바꾸려면 => float(a)
print(res)
# 문자로 표현된 숫자를 정수형으로 바꿈
# 순수 문자를 정수로 바꾸는 건? => 당연히 불가능
# 바꾼 숫자로 계산은 당연히 가능하다 => res+1

# ord
a = 'A'
res = ord(a)
print(res)
# 문자를 아스키코드(정수)로 바꾼다.

# chr
a = 65
res = chr(a//2) # 몫만 나오게 해도 되고 int() 함수를 써준다.
print(res)
# 정수에 해당하는 아스키코드 문자를 반환한다. 
# a = 34로 하고 chr(a*2)로 하면? => 된다
# a = 68로 하고 chr(a/2)로 하면? => 안된다
# 이유는 a/2의 자료형이 float 이기 때문

# ==========================================

# 리스트 함수

# append
res = [1,2,3]
a = [1,2,3]
res = a.append(4)
print(res)
print(a)
# append의 인자를 문자열 뒤에 추가한다.
# a=[1,2,3], res=a.append(4)
# => append가 반환값이 있는 함수가 아니므로 none

# sort 
res1 = ['e','a','h']
res2 = [1,6,2]
res1.sort()
res2.sort(reverse=True) # True라고 정확히 입력해야 함
print(res1)
print(res2)
res3 = sorted(res1) #외부정렬(반환값 있음)
res4 = sorted(res1,reverse = True)
res1.reverse() # 차순 바꾸기  # 당연히 반환값이 없는 함수
print(res1)
print(res2)
print(res3)
print(res4)
# sorted는 딕셔너리 정렬이 가능하다
a = {'2':'B','1':'A','3':'U'}
a1 = sorted(a)
print(a1)

# insert
res = [100,123,523]
res.insert(1,2) 
print(res)
# 특정 인덱스의 값이 되도록 요소를 추가한다. (특정 인덱스 자리에 요소를 추가한다.)
# 계산값을 넣어도 된다.

# remove
res = [10,20,30,40,10]
res.remove(10)
print(res)
# 함수의 인자값을 찾아서 삭제한다.
# 값이 여러개라면? => 가장 첫 번째 요소를 삭제한다.

# pop
res = [10,20,30,40]
a = res.pop() # 반환값이 있는 함수
print(a)
# 마지막 요소를 삭제하는 함수
# 반환값이 잇으므로 변수에 pop한 값을 저장할 수 있음

# count
a = [10,10,101,102,10,'ab']
res = a.count(10)
print(res)
# 함수의 인자값을 찾아서 개수를 센다.
# 내부의 계산값을 넣어도 될까? res = a.count(5+5) => 가능 (정수이므로)

# ================================================

# 딕셔너리 함수

# keys
a = {'a':123,'b':456}
res = a.keys()
print(res)
# 딕셔너리의 key들을 반환한다.

# values
a = {'a':123,'b':456}
res = a.values()
print(res)

# keys
a = {'a':123,'b':456}
res = a.items()
print(res)

# dict~~ 라는 말을 없애고 싶다면 ? => list를 활용한다.

# get
a = {'q':123,'w':456}
res = a.get('t',789) #ㅇ 없는 값이면 789 반환 / 있으면 해당 값 반환 
print(res)
#print(a['t'])
# 둘의 차이는? 키가 없는 값을 반환한다면?
# get 함수를 쓸 때 키가 없는 값을 찾으면 none
# 그냥 딕셔너리에서 키 값으로 찾았을 때 없으면 오류
# get 함수는 키 값이 있다면 그 value를 반환하고
# 없으면 기본값을 지정하여 반환할 수 있다

# in
a = {'q':123,'w':456}
print('q'in a)
# 키 값이 있는지 없는지 검사
# 있으면 True, 없으면 False
# 이 결과를 가지고 if(~~~==True) 로 사용 가능 