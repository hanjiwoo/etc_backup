from subprocess import run
from opencvloc import locateCenterImage
import pyautogui as py # 라이브러리 대체 
import time

run(['calc'])

time.sleep(1)

# x,y=locateCenterImage('5.png')
# py.click(x,y)
# x,y=locateCenterImage('plus.png')
# py.click(x,y)
# x,y=locateCenterImage('3.png')
# py.click(x,y)
# x,y=locateCenterImage('equal.png')
# py.click(x,y)

for i in range(1,10):
		i=str(i)
		x,y=locateCenterImage(i+'.png')
		py.click(x,y)
		if int(i)!=9:
			x,y=locateCenterImage('plus.png')
			py.click(x,y)

x,y=locateCenterImage('equal.png')
py.click(x,y)
