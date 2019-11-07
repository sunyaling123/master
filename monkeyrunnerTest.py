###目标是实现一个打开关闭电子书并执行三次

import random
import os
import time
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device=MonkeyRunner.waitForConnection()
##device.installPackage("/Users/luojilab/Downloads/data/monkeyruner/app_debug_7.4.0_monkey.apkk")

device.startActivity(component="com.luojilab.player/com.luojilab.business.welcome.WelcomeActivity")
MonkeyRunner.sleep(5)
file_object = open('/Users/luojilab/Downloads/data/monkeyruner/log.txt', 'w+')
print("=========shouye===========")
device.touch(540,703,"DOWN_AND_UP")
print("#########dianzishu########")
MonkeyRunner.sleep(5)

num = 0
while (num < 3):
	device.touch(892,1799,"DOWN_AND_UP")
	MonkeyRunner.sleep(5)	
	device.press('KEYCODE_BACK',device.DOWN_AND_UP)
	num += 1
	file_object.write(str("value:")+str(num)+'\n')
	file_object.writelines(time.asctime(time.localtime(time.time()))+'\n')
	file_object.write('logcat -v time *:W ' + '\n')

file_object.close()
