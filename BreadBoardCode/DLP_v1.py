import io
import os
import time
from PIL import Image
import subprocess

	#Need a program with a .exe that can open pictures
#viewer = subprocess.Popen('notepad.exe')
#time.sleep(5)
#viewer.terminate()

	#No way to close this


for i in range(4):
	traces = Image.open('trace_' + str(i) + '.jpg').show()
	time.sleep(1)

	#Arguments for kill function
#os.system('traces.jpg')
#os.kill('traces.jpg')