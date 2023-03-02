# With this program you can cheat on reaction speed test
# found here: https://humanbenchmark.com/tests/reactiontime
import pyautogui
# Press CTRL + C to end program
pyautogui.FAILSAFE = True

screenSize = pyautogui.size()
screenWidth = screenSize[0]
screenHeight = screenSize[1]


while(True):
    mouseX = int(pyautogui.position()[0])
    mouseY = int(pyautogui.position()[1])
    pixel = str(pyautogui.pixel(mouseX, mouseY))
    if pixel == "(75, 219, 106)": # Green
        pyautogui.click()
        pyautogui.sleep(0.1)
        pyautogui.click()
        pyautogui.sleep(2)