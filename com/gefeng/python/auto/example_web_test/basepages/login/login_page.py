# coding=utf-8
from common import base_page
from selenium.webdriver.common.by import By


class Login(base_page):
    # 定位登录页面的用户名输入框
    username_loc = (By.NAME, "username")
    # 定位登录页面的密码输入框
    password_loc = (By.NAME, "password")
    # 定位登录页面的登录按钮
    submit_loc = (By.XPATH, "//form[@class=login-form]/div[2]/div[5]/button")
    # 用户名或密码错误提示信息
    error_msg_loc = (By.ID, 'username-error')

    error_msg_loc = (By.ID, 'password-error')

    # 输入用户名，调用type对象
    def input_username(self, username):
        self.type(self.username_loc, username)

    def input_password(self, password):
        self.type(self.password_loc, password)

    def click_submit(self):
        self.click(self.submit_loc)

    def get_errormessage(self):
        return self.get_text(self.error_msg_loc)




