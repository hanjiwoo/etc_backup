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
	news_list = news.find_elements_by_tag_name('dl')
	# blogs_list의 자료형은 list가 된다

	for article in news_list:
		# print(post.text)
		# print('-'*20)

		article_title = article.find_element_by_class_name('_sp_each_title')		
		print(article_title.text)
		print(article_title.get_attribute('title'))
		print(article_title.get_attribute('href'))
		print('-'*20)
		
		
except Exception as e:
	print(e)

finally:
	driver.close()

