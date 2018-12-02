# 크롤링 수행평가
# 크롤링 할 요소 : 네이버 영화 페이지의 현재 상영중인 영화 제목

# 목적 : 갑자기 영화가 보고 싶을 때, 직접 페이지에 들어가서 상영중인 영화가 무엇이 있는지 찾아보기
# 귀찮을 때, 그런 귀찮음을 없애기 위해 실행만 시키면 현재 상영하는 영화가 무엇이 있는지 
# 출력하는 프로그램

# 동작 과정 : 
# 네이버 영화 메인 페이지에 들어간 후(들어가면 영화 홈 페이지가 떠 있는다) => .get('네이버 영화 페이지 주소') 
# 왼쪽에 있는 상영작/예정작 탭을 누른다(현재 상영영화 페이지가 떠 있는다) => .click() : 클래스명으로 찾은 요소를 클릭한다. ('menu02' : 상영작/예정작 탭 클래스명)
# 영화 전체 목록 요소를 클래스명으로 찾은 후 받아 온 후 => 클래스 명 : 'lst_wrap'
# 각 영화 목록(li 태그들)을 list 형태로 받아온다 => movie_lists 

# <볼 수 있는 연령과 제목을 함께 받아오고 싶을 때>
# 영화 목록(li 태그)에서 클래스명으로 연령가와 제목을 찾아서 받아온다. => class_name('tit') => 연령가와 제목이 dt 태그로 묶여 있는데 dt 태그의 클래스명이 'tit'이다
# <제목만 받아오고 싶을 때>
# 영화 목록(li)에서 제목(a태그)만 받아온다. * 제목에 해당하는 클래스명이 없기 때문에 a태그로 찾아서 받아와야 하는데 li 태그 안에
# a 태그가 2개가 있기 때문에 xpath를 사용해 li 태그 안의 dl 태그 안의 dt 태그 안에 있는 a태그(영화 제목에 해당하는)만 받아온다. => xpath('./dl/dt/a')

# 받아온 제목은 list 타입이기 때문에 text로 바꿔주고 콘솔 창에 출력한다. => movie_title(제목 받아온 변수).text
# 받아온 제목을 엑셀 파일에 넣기 => sheet.append([movie_title.text])
# 그 후 엑셀파일을 저장한다. => wb.save('파일명.xlsx')

# try-except 문으로 예외처리를 해주고 finally문으로 실행이 끝나면 크롬 창을 끄도록 한다. => driver.close()

# 기대 효과 :
# 실행만 시키면 현재 상영하는 영화들을 출력해주기 때문에 이번에 상영하는 영화를 보고 싶지만 뭐 하는지를 
# 모르는 사람이나 그것조차 찾기 귀찮은 사람들에게는 해당 프로그램은 편리할 것이다.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')
wb = Workbook()
sheet = wb.active

try :
	driver.get('https://movie.naver.com/')
	print(driver.title)

	driver.find_element_by_class_name('menu02').click()

	movie = driver.find_element_by_class_name('lst_wrap')
	movie_list = movie.find_elements_by_tag_name('li')

	for movie in movie_list:
		movie_title = movie.find_element_by_class_name('tit')   # 관람 가능한 연령과 제목 같이 받아 올때 
		# movie_title = movie.find_element_by_xpath('./dl/dt/a') # 제목만 받아올 때
		print(movie_title.text)
		print('-'*20)
		sheet.append([movie_title.text])

	wb.save('20420_자유.xlsx')

except Exception as e:
	print(e)

finally:
	driver.close()