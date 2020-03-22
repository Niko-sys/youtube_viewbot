import webbrowser
import time
import os
import optparse

wait_time = 3 # time to wait until video is laoded and played

parser = optparse.OptionParser()
parser.add_option('-u', dest='url', type='string', default="https://www.youtube.com/watch?v=yOpF54plrM0")
parser.add_option('-v', dest='view', type='int', default=3)
parser.add_option('-t', dest='time', type='int', default=10)
(options, args) = parser.parse_args()
print(options.url, options.view, options.time)

controller = webbrowser.get()

for i in range(options.view):
	controller.open(options.url)
	time.sleep(wait_time)

time.sleep(options.time)
os.system("killall -9 'Google Chrome'")
