from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('http://dsm2015.cafe24.com/#/')
	print(driver.title)

	title_id = driver.find_element_by_id('meal-content-wrapper')

	meal_list = title_id.find_elements_by_class_name('meal-content')

	for meals in meal_list:
		print(meals.text)

except Exception as e:
	print(e)

finally:
	# 브라우저 종료
	driver.quit()