#coding=utf-8
import sys
sys.path.append("C:\\Users\\miss\\.jenkins\\workspace\\Android UI automation")

import unittest
from jioben.test1 import Loong
from jioben.test2 import Loong2
import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Loong))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Loong2))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ceshi1))
    # 这一步是在当前文件夹里自动生成一个测试报告
    with open('HTMLReport.html', 'wb') as f:
        runner =HTMLTestRunner.HTMLTestRunner(stream=f,
                                               title='Android自动化测试',
                                               description='测试回馈报告.',
                                               verbosity=2
                                               )
        runner.run(suite)
