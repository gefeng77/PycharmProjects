# coding=utf-8

import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import re
import log


class BaseObject(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些页面常用都操作方法到这个类
    """
    def __init__(self, driver):
        self.driver = driver
        self.mylog = log()

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        self.mylog.info("Click forward on current page.")

    def back(self):
        self.driver.back()
        self.mylog.info("Click back on current page.")

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        self.mylog.info("Wait for %s minutes." % seconds)

    def close(self):
        try:
            self.driver.close()
        except NameError as e:
            self.mylog.info("Fail to quit the browser with %s." % e)

    def img_screenshot(self, img_path, img_file):
        try:
            self.driver.get_screenshot_as_file(img_path+img_file+".png")
        except:
            self.mylog.info("%s截图失败。" % img_file)

    def current_window(self):
        all_handlers = self.driver.window_handlers
        for handler in all_handlers:
            self.driver.swith_to.window(handler)

    # 重写find_element()方法，增加定位元素的健壮性
    def find_element(self, *selector):
        try:
            # 确保元素是可见的
            # 注意：以下入参为元组的元素，需要加*，python存在这种特性，就是将入参放在元组中
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(selector))
            print("find_element(*selector)", self.driver.find_element(*selector))
            return self.driver.find_element(*selector)
        except:
            self.mylog.info("定位元素失败")

    def type(self, selector, text):
        try:
            el = self.find_element(*selector)
            el.clear()
            el.send_keys(text)
        except NameError as e:
            self.mylog.info("Fail to type in input box with %s" % e)

    def click(self, selector):
        try:
            el = self.find_element(*selector)
            el.click()
            sleep(3)
        except NameError as e:
            self.mylog.info("Fail to type in input box with %s" % e)

    # 通过value获取下拉菜单并点击
    def select_element_text(self, selector, text):
        try:
            el = self.find_element(*selector)
            Select(el).select_by_value(text)
        except:
            self.mylog.info("Cann't find the element by text %s" % str(selector))

    #  通过index获取下拉菜单并点击
    def select_element_index(self, selector, index):
        try:
            el = self.find_element(*selector)
            Select(el).select_by_index(index)
        except:
            self.mylog.info("Cann't find the elment by index %s" % str(selector))

    # 获取元素的属性值
    def get_attribute(self, selector, value):
        el = self.driver.find_element(selector).get_attribute(value)
        return el

    def get_text(self, selector, text):
        el = self.driver.find_element(selector).text()
        return el

    # 检验按钮是否为选中状态
    def is_selected(self, selector):
        el = self.find_element(*selector)
        if el.is_selected:
            self.mylog.info(el+"被选中")
        else:
            self.mylog.info("请重新选择")

    # 获取网页标题
    def get_page_title(self, title):
        return self.driver.title()
