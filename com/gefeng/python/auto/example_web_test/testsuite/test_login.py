# coding=utf-8
import unittest
import os
# 当前程序上上一级目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.append(base_path)
import common.base_page
import basepages.login.login_page
from common.bse_page import *
from basepages.login.login_page import *


class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        self.driver.browser("sbc")

    @classmethod
    def tearDownClass(cls) -> None:
        self.driver.quit()

    def login(self, username, password):
        self.driver.current_window_handle
        self.login_page.input_username(username)
        self.Login.input_password(password)
        self.Login.click_submit()
        sleep(2)

    def test_loginfailure(self):
        try:
            self.login()
            self.driver.current_window_handle
            error_message = self.login_page.get_errormessage()
            # self.login_page.confirm_btn()
            self.assertIn('Username is required', error_message)

        except Exception as e:
            self.login_page.img_screenshot(u'用户名密码为空')
        raise e

    def test_bracnch(self):
<<<<<<< HEAD
        print("Now it is on the master branch.")
=======
        print("Now it is on the message_change branch")
>>>>>>> new_change


