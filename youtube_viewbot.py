import webbrowser
import time
import os

controller = webbrowser.get()

for i in range(5):
	controller.open("https://www.youtube.com/watch?v=yOpF54plrM0")
	time.sleep(3)

time.sleep(300)
os.system("killall -9 'Google Chrome'")