import unittest
from appium import webdriver
import time
from bao.HTMLTestRunner3_New import HTMLTestRunner
import os


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',  # 平台系统：Android or Ios
            'deviceName': 'OPPO R11',  # 设备名称
            'platformVersion': 'android-4.4W',  # 平台版本
            'appPackage': 'com.baidu.yuedu',  # 包名
            'appActivity': 'com.baidu.yuedu.splash.SplashActivity',  # activity
            'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串 }
            'resetKeyboard': True}  #
        self.d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(15)

    def tearDown(self) -> None:
        time.sleep(5)
        self.d.quit()

    def test_1(self):
        self.d.find_element_by_id(r'com.baidu.yuedu:id/righttitle').click()
        time.sleep(8)
        # self.d.find_element_by_xpath("//android.widget.RelativeLayout[@index='2']").click()
        # time.sleep(5)
        size = self.d.get_window_size()
        # x=size.get('width')*0.5
        # y=size.get('height')*0.2
        # y1=size.get('height')*0.8
        y = size.get('height') * 0.5
        x1 = size.get('width') * 0.9
        x = size.get('width') * 0.1
        for i in range(3):
            self.d.swipe(x1, y, x, y, 1000)
            time.sleep(3)

    def test_2(self):
        self.d.find_element_by_id(r'com.baidu.yuedu:id/righttitle').click()
        time.sleep(8)
        self.d.find_element_by_xpath("//android.widget.RelativeLayout[@index='2']").click()
        time.sleep(5)
        size = self.d.get_window_size()
        x = size.get('width') * 0.5
        y = size.get('height') * 0.2
        y1 = size.get('height') * 0.8
        for i in range(3):
            self.d.swipe(x, y1, x, y, 1000)
            time.sleep(3)

    def test_3(self):
        self.d.find_element_by_id('com.baidu.yuedu:id/search_account').click()
        time.sleep(5)
        self.d.find_element_by_xpath("//android.widget.EditText[@text='搜书架或书城']").send_keys('斗罗大陆')

    def test_4(self):
        self.d.find_element_by_id('com.baidu.yuedu:id/title_account').click()
        time.sleep(5)
        self.d.find_element_by_id('com.baidu.yuedu:id/hack_tx_account_name').click()
        time.sleep(5)
