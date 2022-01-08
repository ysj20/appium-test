import unittest
import selenium
import time
from appium import webdriver
from huaping import huadong

class Loong2(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        #手机设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '7SAYLJ75Z9A6BMJ7'
        desired_caps['appPackage'] = 'com.duowan.kiwi'
        #desired_caps['appPackage'] ='com.tencent.qqlive'
        #desired_caps['appPackage'] = 'com.tencent.news'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.duowan.kiwi.homepage.Homepage'
        #desired_caps['appActivity'] = 'com.tencent.qqlive.ona.activity.SplashHomeActivity'
        #desired_caps['appActivity'] = 'com.tencent.news.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
    def testhuya(self):
        time.sleep(5)
        self.driver.find_element_by_id("com.duowan.kiwi:id/search_text").click()
        time.sleep(6)
        self.driver.find_element_by_id("com.duowan.kiwi:id/search_content").send_keys("小超梦z").click()
        time.sleep(7)
        self.driver.find_element_by_id("com.duowan.kiwi:id/search_btn").click()
        time.sleep(10)

        #截图
        self.driver.save_screenshot("yun.png")
        self.driver.get_screenshot_as_file(r"E:\appium-test\screenshot/feng.png")
        #上下左右滑动
        huadong.swipeUp(self.driver)
        time.sleep(3)
        huadong.swipeDown(self.driver)
        time.sleep(3)
        huadong.swipRight(self.driver)
        time.sleep(3)
        huadong.swipLeft(self.driver)
        time.sleep(3)
        huadong.swipRight(self.driver)
        time.sleep(3)
        huadong.swipLeft(self.driver)
        time.sleep(3)
        huadong.swipeDown(self.driver)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Loong2)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()