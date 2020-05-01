# coding=utf-8
import unittest

from HTMLTestRunner import HTMLTestRunner
from com.gefeng.python.unittest_example.function import *


class TestFunction(unittest.TestCase):

    # 每执行一个case都会运行一遍
    # def setUp(self) -> None:
    #     print("Do something before test, preparing environment")

    # 仅运行一次
    @classmethod
    def setUpClass(cls) -> None:
        print("Do something before test, preparing environment")

    # @unittest.skip("Just don't run this testcase with no reason.")
    def test_add(self):
        print("add")
        self.assertEqual(5, add(3, 2))
        self.assertNotEqual(5, add(2, 2))

    # @unittest.skipIf(3>2, "If True, system will not run this case.")
    def test_minus(self):
        print("minus")
        self.assertEqual(3, minus(5, 2))

    @unittest.skipUnless(3>2, "If False, system will run this case.")
    def test_multi(self):
        print("multi")
        self.assertEqual(8, multi(2, 4))

    def test_divide(self):
        # self.skipTest("do not run test_divide()")
        print("divide")
        self.assertEqual(5, divide(10, 2))
        self.assertEqual(2.5, divide(5, 2))

    # def tearDown(self) -> None:
    #     print("do something after test: clean up")

    @classmethod
    def tearDownClass(cls) -> None:
        print("do something after test: clean up")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    # 按照suite套件里指定的顺序执行
    tests = [TestFunction("test_add"), TestFunction("test_minus"), TestFunction("test_multi"), TestFunction("test_divide")]
    suite.addTests(tests)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 执行指定路径下的测试脚本
    # file_path = "./"
    # discover = unittest.defaultTestLoader.discover(file_path, "test_function.py")
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(discover)

    # 生成txt的测试报告
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFunction))
    # report_path = "/users/air/PycharmProjects/TestReport/HTMLTestReport.txt"
    # with open(report_path, 'w') as UnittestTextReport:
    #     runner = unittest.TextTestRunner(stream=UnittestTextReport, verbosity=2)
    #     runner.run(suite)

    # unittest.main(verbosity=2)

    # 生成html的测试报告，配置后才会运行

    # 存放测试报告的路径
    report_path = "/users/air/PycharmProjects/TestReport/HTMLTestReport.html"
    with open(report_path, "w") as file:
        runner = HTMLTestRunner(stream=file, title="TestReport of web", verbosity=2)
        runner.run(suite)



