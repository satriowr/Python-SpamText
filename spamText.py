import pyautogui
import time

message = "Hello World"
n = 1000

time.sleep(3)

for i in range (n): 
    pyautogui.typewrite(message)
    pyautogui.press('enter')

                 
