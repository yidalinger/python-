from appium import webdriver
from time import *
import unittest
from bao.HTMLTestRunner3_New import HTMLTestRunner


class TestApp(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            'platformName': 'Android',  # 平台系统：Android or Ios
            'deviceName': 'OPPO R11',  # 设备名称
            'platformVersion': 'android-4.4W',  # 平台版本
            'appPackage': 'com.baidu.yuedu',  # 包名
            'appActivity': 'com.baidu.yuedu.splash.SplashActivity',  # activity
            'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串 }
            'resetKeyboard': True}  # 是将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def tearDown(self):
        sleep(4)
        self.driver.quit()

    def test001(self):
        # self.driver.find_element_by_id("com.baidu.yuedu:id/negativeUpgrade").click()
        sleep(5)
        self.driver.find_element_by_id("com.baidu.yuedu:id/righttitle").click()
        self.driver.get_window_size()
        self.driver.swipe()
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='1']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='更多 Link']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//android.view.View[@index='2']").click()
        sleep(5)
        self.driver.find_element_by_id("com.baidu.yuedu:id/book_add_cart").click()
        sleep(5)
        self.driver.find_element_by_id("com.baidu.yuedu:id/ball").click()


if __name__ == '__main__':
    unittest.main()
    # path=r"F:\untitled\untitled5\shouji"
    # discover = unittest.TestLoader().discover(start_dir=path, pattern='appzdh.py')
    # dir=r'F:\untitled\untitled5\shouji' + '\\' + 'ui.html'
    # filename=open(dir, 'wb')
    # runner = HTMLTestRunner(stream=filename,
    #                         title='UI自动化测试报告',
    #                         description='用例执行情况如下',
    #                         tester='dcs')
