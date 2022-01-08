import unittest
import selenium
import time
from appium import webdriver


class Loong(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '7SAYLJ75Z9A6BMJ7'
        desired_caps['appPackage'] = 'com.smile.gifmaker'
        #desired_caps['appPackage'] = 'com.duowan.kiwi'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.yxcorp.gifshow.HomeActivity'
        #desired_caps['appActivity'] = 'com.duowan.kiwi.adsplash.view.AdSplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
    def testdianshi(self):
        #time.sleep(5)
        #self.driver.find_element_by_id("android:id/content").click()
        time.sleep(5)

        # 获取屏幕宽度和高度
        def get_size():
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            return x, y

        print(get_size())

        # 屏幕向上滑动
        def swipeUp(t):
            l = get_size()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.75)  # 起始y坐标
            y2 = int(l[1] * 0.25)  # 终点y坐标
            self.driver.swipe(x1, y1, x1, y2, t)

        # 屏幕向下滑动
        def swipeDown(t):
            l = get_size()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.25)  # 起始y坐标
            y2 = int(l[1] * 0.75)  # 终点y坐标
            self.driver.swipe(x1, y1, x1, y2, t)

        # 屏幕向左滑动
        def swipLeft(t):
            l = get_size()
            x1 = int(l[0] * 0.75)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.05)
            self.driver.swipe(x1, y1, x2, y1, t)

        # 屏幕向右滑动
        def swipRight(t):
            l = get_size()
            x1 = int(l[0] * 0.05)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.75)
            self.driver.swipe(x1, y1, x2, y1, t)


        # 调用向左滑动
        swipLeft(2000)
        print("向左滑动")
        time.sleep(3)
        # 调用向右滑动
        swipRight(2000)
        print("向右滑动")
        time.sleep(6)
        swipRight(2000)
        print("向右滑动")
        time.sleep(6)
        swipeUp(2000)
        print("向右滑动")
        time.sleep(6)
        # 调用向左滑动
        swipLeft(2000)
        print("向左滑动")
        time.sleep(6)
        # 调用向上滑动
        swipeUp(2000)
        print("向上滑动")
        time.sleep(6)
        swipeUp(2000)
        print("向上滑动")
        time.sleep(5)
        swipeUp(2000)
        print("向上滑动")
        time.sleep(5)
        # 调用向下滑动
        swipeDown(2000)
        print("向下滑动")
        time.sleep(3)
        swipeDown(2000)
        print("向下滑动")
        time.sleep(3)

        self.driver.save_screenshot("yun.png")
        self.driver.get_screenshot_as_file(r"E:\appium-test\screenshot/feng.png")

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Loong)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()