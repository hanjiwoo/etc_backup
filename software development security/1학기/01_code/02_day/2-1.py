>>> a=3
>>> a
3
>>> print(a)
3
>>> type(a)
<class 'int'>
>>> print(type(a))
<class 'int'>
>>> a=3.14
>>> type(a)
<class 'float'>
>>> b=6
>>> a
3.14
>>> b
6
>>> c=a+b
>>> type(c)
<class 'float'>
>>> a="준현"
SyntaxError: EOL while scanning string literal
>>> a="준현"
>>> b="부영"
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
'준현'
>>> b
'부영'
>>> a+b
'준현부영'
>>> c="어영"
>>> a
'준현'
>>> a+b+c
'준현부영어영'
>>> def c():
	print("\n"*10)

	
>>> c()











>>> def clear():
	print("\n"*20)

	
>>> 
>>> dffdf
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dffdf
NameError: name 'dffdf' is not defined
d
>>> fd
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    fd
NameError: name 'fd' is not defined
>>> df
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    df
NameError: name 'df' is not defined
d
>>> f
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> clear()





















>>> print("연산자 실습")
연산자 실습
>>> ㅁ=11
>>> a=11
>>> b=2
>>> a+b
13
>>> a-b
9
>>> a*b
22
>>> a/bb
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a/bb
NameError: name 'bb' is not defined
>>> a/b
5.5
>>> a**b
121
>>> b=3
>>> a**b
1331
>>> b=2
>>> a%b
1
>>> a//b
5
>>> a=-11
>>> a
-11
>>> b
2
>>> a//b
-6
>>> a//b+1
-5
>>> print("정확한 몫 구하기")
정확한 몫 구하기
>>> a=-10
>>> a//b
-5
>>> print("문자열")
문자열
>>> a='성운'
>>> ㅁ
11
>>> a
'성운'
>>> print(a)
성운
>>> a=''성운''
SyntaxError: invalid syntax
>>> a=
SyntaxError: invalid syntax
>>> a="'성운'"
>>> a
"'성운'"
>>> print("쌍따옴표 안에 호따옴표 넣기 반대도 가능")
쌍따옴표 안에 호따옴표 넣기 반대도 가능
>>> a='"성운"'
>>> ㅁ
11
>>> a
'"성운"'
>>> a=' "성운" '
>>> ㅁ
11
>>> a
' "성운" '
>>> print(a)
 "성운" 
>>> a=''' 성운이
          어영부영'''
>>> ㅁ
11
>>> a
' 성운이\n          어영부영'
>>> print(a)
 성운이
          어영부영
>>> a=''' "성운이
          어영부영"'''
>>> print(a)
 "성운이
          어영부영"
>>> a="adfdfdeaghegwagewge \n dfdfafdfdfdfddf"
>>> print(a)
adfdfdeaghegwagewge 
 dfdfafdfdfdfddf
>>> a=""" dfdggqgq  '' dfdf ewet  \n dfdsafefage
dfadfegawehag edfafe 'dfdfaeg'fe
dfadfa"""
>>> print(a)
 dfdggqgq  '' dfdf ewet  
 dfdsafefage
dfadfegawehag edfafe 'dfdfaeg'fe
dfadfa
>>> a="one"
>>> b="three"
>>> b="light"
>>> print(a+b)
onelight
>>> print(a+' jun '+b)
one jun light
>>> print(a+' "jun" '+b)
one "jun" light
>>> a='-'*60
>>> print(a)
------------------------------------------------------------
>>> a='-'
>>> print(a*60)
------------------------------------------------------------
>>> clear()





















>>> a="jjjw is god"
>>> a="jjw is god"
>>> print("공백도 인덱스 값 들어감 총, 10개")
공백도 인덱스 값 들어감 총, 10개
>>> a[0]
'j'
>>> a[3]
' '
>>> print(a[0])
j
>>> print(a[3])
 
>>> print("인덱싱")
인덱싱
>>> print(a[0]+a[1]+a[2]+a[4]+a[5]+a[9])
jjwisd
>>> a='2018-3-13 11:16'
>>> print(a)
2018-3-13 11:16
>>> a='2018-03-13 11:16'
>>> print("슬라이싱")
슬라이싱
>>> print(a[0])
2
>>> print(a[0:3])
201
>>> print(a[0:4])
2018
>>> print(a[0:])
2018-03-13 11:16
>>> print(a[:])
2018-03-13 11:16
>>> print(a[5:])
03-13 11:16
>>> print(a[:7])
2018-03
>>> clear()





















>>> a=[0,123,'aaa',111,1,1]
>>> type(a)
<class 'list'>
>>> print(a[1])
123
>>> print(a[4])
1
>>> a=[0,123,'aaa',111,1.1]
>>> print(a[4])
1.1
>>> type(a[4])
<class 'float'>
>>> print(a[2:])
['aaa', 111, 1.1]
>>> print(a[1]+' and '+a[3:])
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    print(a[1]+' and '+a[3:])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a[1],' and ',a[3:])
123  and  [111, 1.1]
>>> print(a[-1])
1.1
>>> clear()





















>>> dic={'1':'min','2':'gyu','10':'one'}
>>> dic['1']
'min'
>>> print(dic['10'])
one
>>> a='DSMBY'
>>> a='DSMBY'
>>> a='refrigerator'
>>> r=a.count(r)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    r=a.count(r)
NameError: name 'r' is not defined
>>> r=a.count("r")
>>> print(r)
4
>>> r=a.find("r")
>>> print(r)
0
>>> r=a.index("r")
>>> print(r)
0
>>> r=a.join("r")
>>> a='.'
>>> a=','
>>> r=a.join("dsm")
>>> print(r)
d,s,m
>>> clear()





















>>> clear()





















>>> a='banana monkey'
>>> a.count(a)
>>> a.count("a")
3
>>> a.count("n")
3
>>> a.count("m")
1
>>> a.find("n")
2
>>> a.find("m")
7
>>> a.index("d
	
SyntaxError: EOL while scanning string literal
>>> a.index("d")
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    a.index("d")
ValueError: substring not found
>>> a.find("d")
-1
>>> b=','


>>> b
','
>>> a.join(b)
','
>>> a
'banana monkey'
>>> print(a.join(b))
,
>>> b=','
>>> print(a.join(b))
,
>>> b=a.join(',')
>>> print(b)
,
>>> b=a.join(",")
>>> b
','
>>> b=','
>>> r=b.join(a)
>>> print(r)
b,a,n,a,n,a, ,m,o,n,k,e,y
>>> print(a.upper())
BANANA MONKEY
>>> b="BANNA MONKEY"
>>> print(b.lower())
banna monkey
>>> print(a.replace("banana","apple"))
apple monkey
>>> a="      apple monkey
SyntaxError: EOL while scanning string literal
>>> a="      apple monkey      "
>>> a.split()
['apple', 'monkey']
>>> a="applemonkey"
>>> a.split()
['applemonkey']
>>> a="apple monkey"
>>> a.split()
['apple', 'monkey']
>>> a="      apple monkey      "
>>> a.lstrip()
'apple monkey      '
>>> a.rstrip()
'      apple monkey'
>>> a.strip()
'apple monkey'
>>> a.type()
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    a.type()
AttributeError: 'str' object has no attribute 'type'
>>> type(a)
<class 'str'>
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '      apple monkey      '
>>> a='12334'
>>> int(a)
12334
>>> a
'12334'
>>> b=65489
>>> str(b)
'65489'
>>> b
65489
>>> ord(65)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    ord(65)
TypeError: ord() expected string of length 1, but int found
>>>
