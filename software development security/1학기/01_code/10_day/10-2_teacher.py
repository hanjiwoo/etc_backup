from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome('chromedriver')

try : 
	driver.get('http://www.naver.com')
	print(driver.title)

	elem = driver.find_element_by_id('query')
	elem.clear() 
	# clear()를 해주는 이유는 간혹 포털마다
	# 검색어가 이미 입력되어있는 경우가 있기 때문 
	elem.send_keys('대덕소프트웨어마이스터고')
	elem.send_keys(Keys.RETURN)

	news = driver.find_element_by_class_name('news')
	news_list = news.find_elements_by_tag_name('li')
	# news_list = news.find_elements_by_tag_name('li')
	# 위와 같이 코드를 작성하게 되면
	# li 태그를 가진 하위 뉴스 리스트까지 불러오게 됨
	# 오류 발생
	news_list = news.find_elements_by_xpath('./ul/li')
	# xpath를 활용하여 경로를 지정해준다 
	# ul 태그 밑에 있는 li 태그만을 가져오겠다는 의미 
	
	for news in news_list:
		# print(post.text)
		# print('-'*20)

		news_title = news.find_element_by_class_name('_sp_each_title')		
		print(news_title.text)
		# print(article_title.get_attribute('title'))
		print(news_title.get_attribute('href'))
		print('-'*20)
		
		
except Exception as e:
	print(e)

finally:
	driver.close()

