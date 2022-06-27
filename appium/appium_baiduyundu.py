from appium import webdriver
from time import *

desired_caps = {
    'platformName': 'Android',  # 平台系统：Android or Ios
    'deviceName': 'OPPO R11',  # 设备名称
    'platformVersion': 'android-4.4W',  # 平台版本
    'appPackage': 'com.baidu.yuedu',  # 包名
    'appActivity': 'com.baidu.yuedu.splash.SplashActivity',  # activity
    'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串 }
    'resetKeyboard': True}  # 是将键盘隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(15)
driver.find_element_by_id(r'com.baidu.yuedu:id/righttitle').click()
sleep(8)
driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='2']").click()
sleep(5)
size = driver.get_window_size()
# x=size.get('width')*0.5
# y=size.get('height')*0.2
# y1=size.get('height')*0.8
y = size.get('height') * 0.5
x1 = size.get('width') * 0.9
x = size.get('width') * 0.1
for i in range(3):
    driver.swipe(x1, y, x, y, 1000)
    sleep(3)

driver.quit()
