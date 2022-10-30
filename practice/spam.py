#a program for annoying spamming chat bot
import pyautogui ,time
message = input("enter :")
limit = int(input('enter no. of repeats'))

for i in range(limit):
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(0.0001)