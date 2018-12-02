<h4>수업 1일차 보고서</h4>


# <h3> python 설치 </h3>

1. python 사이트( https://www.python.org/ )에 접속한다.
2. 페이지를 내리다 보면 downloads 와 latest : python 3.64가 보이고 클릭하여 들어간다.
3. files version에서 5번째 항목(Windows x86-64 executable installer)을 선택하여 설치한다.
4. 설치가 완료되면 lnstaller가 뜨며 next를 누르며 python 설치를 진행한다.
(이때 path를 자동으로 설정해준다는 항목을 선택 후 설치를 진행한다. 하지 않는다면 직접 path를 설정해야한다.)

# <h3> sublime text(version 3) 설치 과정 </h3>

1. sublime text 사이트( https://www.sublimetext.com/ )에 접속한다. 
2. 오른쪽 위에서 download를 찾고 그 페이지에 들어간다.
3. OS X, windows, windows 64bit, linux 중 windows를 선택한다.
(손상시킬 수 있는 파일이라고 뜰 수 있는데 그냥 계속 다운로드를 한다.)
4. 계속 next를 누르다가 설치 될 위치를 d드라이브로 설정하고 다운로드를 완료한다.

# <h3> hello world 출력 </h3>

- 새 python 파일 생성
1. sublime text를 연다(실행한다).
2. 아무것도 하지 않은 상태에서 ctrl + s(저장)를 눌러 저장한다.
(이때 파일명은 자신이 원하는 명으로 하며 확장자는 py(python)로 파일명.py로 저장한다.)
3. 새 파일이 생성 되면 자신이 원하는 코드를 입력하고 저장한다.

- code 짜기 <br/>
python에서의 출력은 print()를 사용하며 ;(세미콜론)를 사용하지 않는다. 문자열을 쓸 때는 c처럼 “”안에 쓰며 hello world 출력을 위한 문장은 print(“hello world”) 이다.
print(“hello world”) 

# <h3> python 파일 실행시키기 </h3>

자신이 python 파일을 만든 폴더에 들어가 shift + 오른쪽 클릭(마우스)을 하면 ‘여기에 powershell 창 열기’ 항목이 나온다.(그냥 오른쪽 클릭하면 나오지 않는다.) shell 창을 열고 ‘python 파일명.py’를 치면 “hello word“ 가 출력된다.

- python 파일이 있는 폴더에 들어가기 -> shift + 오른쪽 클릭 -> 여기에 powershell 창 열기 -> python 파일명.py 
-----------------------------------------------------------------------------
# 주석 / sublime text 단축키

python에서의 주석은 ‘#’을 사용하여 쓰며 즉, #adfdfdf 라고 쓰면 주석처리가 된다. 하나하나 #을 써서 주석하기 번거로울 때는 ctrl + /를 사용하면 커서가 있는 줄에 주석처리가 된다. 여러 줄을 주석처리하고 싶을 때는 시작할 부분에 ”“” 또는 ‘’‘ 를 쓰고 마칠 부분에도 ’‘’를 사용하면 주석처리가 된다. 
1. '#'
2. ctrl + /
3. ‘’‘ or “”“