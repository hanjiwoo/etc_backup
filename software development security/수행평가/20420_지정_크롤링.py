from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')
wb = Workbook()
sheet = wb.active

try :
	driver.get('http://www.11st.co.kr/html/main.html')
	print(driver.title)

	elem = driver.find_element_by_class_name('header_inp_txt')
	elem.clear()

	elem.send_keys('라즈베리파이')
	elem.send_keys(Keys.RETURN)

	product = driver.find_element_by_class_name('hotClick_wrap')
	product_list = product.find_elements_by_tag_name('li')

	for product in product_list:
		product_title = product.find_element_by_class_name('info_tit')
		print(product_title.text)
		print('-'*20)
		sheet.append([product_title.text])

	wb.save('20420_지정.xlsx')

except Except as e:
	print(e)
finally :
	driver.close()