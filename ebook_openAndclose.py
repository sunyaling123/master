##打开关闭电子书,app是登录状态，进入App首页，点击电子书模块进入电子书首页，再点击首页内一本试读电子书，并打开关闭三次
from uiautomator import device as d
import time


d(resourceId='com.luojilab.player:id/classNameTextView',text='电子书').click.wait()
time.sleep(2)
for i in range(3):
    d(text='试读').click.wait()
    d.press.back()
    time.sleep(1)
