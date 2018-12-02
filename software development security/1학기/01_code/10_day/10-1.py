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

	blogs = driver.find_element_by_class_name('_blogBase')
	blogs_list = blogs.find_elements_by_tag_name('li')
	# blogs_list의 자료형은 list가 된다

	for post in blogs_list:
		# print(post.text)
		# print('-'*20)

		post_title = post.find_element_by_class_name('sh_blog_title')		
		#print(post_title.text)
		print(post_title.get_attribute('title'))
		print(post_title.get_attribute('href'))
		print('-'*20)
		
		# 여기서 한 가지 의문이 들 수가 있다
		# 그 의문을 찾아내 볼 것
		#살펴.... 출력하고 픔
		# => ...으로 title이 생략되어 있는 부분의 제목을 출력하기 => 속성 : title
		# 응용 : 링크 되는 사이트의 URL 을 같이 출력해볼 것
except Exception as e:
	print(e)

finally:
	driver.close()


