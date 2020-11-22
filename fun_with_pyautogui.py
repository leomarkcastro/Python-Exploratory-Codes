import pyautogui as pa
from time import sleep as s

print(pa.position())

#go to desktop
pa.moveTo(1915,1075,1)
pa.click()

#refresh the screen as much as you want
for i in range(0,1):
    pa.moveTo(840,480,0.2)
    pa.click(button = "right")
    pa.moveTo(948,564,0.1)
    pa.click()

#create a text file
pa.moveTo(840,480,0.2)
pa.click(button = "right")
pa.moveTo(1100,732,0.2)
s(1)
pa.moveTo(1285,674,0.5)
pa.click()

#naming the textfile
pa.typewrite("why you so gay", interval = 0.1)
pa.press('enter')
s(1)
pa.press('enter')
s(0.5)
pa.press('alt + tab')

pa.press('')

#type your message
pa.typewrite("just joking\r I love you :)", interval = 0.1)


