import mouseinfo, pyautogui, time

#mouseinfo.mouseInfo()

pyautogui.moveTo(1235, 1064, duration=0.5) #google
pyautogui.click()
pyautogui.moveTo(659, 371, duration=0.5) #pesquisa
pyautogui.click()
time.sleep(1)
pyautogui.write("youtube")
pyautogui.press("ENTER")
pyautogui.moveTo(262, 300, duration=0.5)
pyautogui.click()
pyautogui.moveTo(665, 113, duration=0.5)
time.sleep(6)
pyautogui.click()
pyautogui.write("ah zé da manga")
pyautogui.press("ENTER")
pyautogui.moveTo(543, 375, duration=0.5)
pyautogui.click()
time.sleep(1)
