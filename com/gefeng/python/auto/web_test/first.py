# coding=utf-8
import time
from selenium import webdriver
import logging
from selenium.webdriver.common.keys import Keys


class DriverTest(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_driver(self):
        self.driver.implicitly_wait(30)
        url = "https://i.pauct.com/baseplat/user/login?from=logout&appCode=XIEJIAN"
        self.driver.get(url)
        time.sleep(2)

    def quit_driver(self):
        self.driver.quit()

    def login(self):
        login_name = self.driver.find_element_by_id("loginNo")
        login_name.clear()
        login_name.send_keys("15902112282")
        time.sleep(2)
        password = self.driver.find_element_by_id("password")
        # password.clear()
        password.send_keys("Aa123456")
        submit = self.driver.find_element_by_xpath("//*[@class='ant-btn antd-pro-pages-baseplat-user-login-submitBtn ant-btn-primary ant-btn-block']")
        submit.click()

        windows = self.driver.window_handles
        logging.info(windows)
        logging.basicConfig(level=logging.INFO)
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)

    def pages(self):
        windows = self.driver.window_handles
        print(windows)
        self.driver.switch_to.window(windows[-1])
        result_url = self.driver.current_url
        print(result_url)
        time.sleep(3)
        # "html/body/div/div/div[2]/div/div/div[4]/div/div/div[2]/div/div")
        project = self.driver.find_element_by_xpath("/html/body/div/div/section/main/div/div/div/div[4]/div/div/div[2]/div[1]/div")
        project.click()

        time.sleep(2)
        # 点击【质量问题】标签
        module = self.driver.find_element_by_xpath("//*[@class='antd-pro-pages-baseplat-project-list-appList']/div/div/p[1]")
        # "/html/body/div/div/section/main/div/div/div[1]/div/p[1]")
        module.click()

        time.sleep(2)
        # 点击【新建问题】标签
        new_page = self.driver.find_element_by_xpath("/html/body/div/div/section/main/div/div/div[1]/div[4]/div/div/p[2]")
        new_page.click()

    def new_question(self):
        time.sleep(2)
        name = self.driver.find_element_by_xpath("/html/body/div/div/section/main/div/form/div[2]/div[1]/div[1]/div[2]/div/span/input")
        # 利用时间戳生成唯一的问题名称
        name.send_keys("test_"+time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
        time.sleep(2)
        leibie = self.driver.find_element_by_xpath("/html/body/div/div/section/main/div/form/div[2]/div[1]/div[2]/div[2]/div/span/div/span/span[1]")
        leibie.click()

        # 选择问题分类
        dialog = self.driver.find_element_by_class_name("ant-modal")
        summary = dialog.find_element_by_class_name("ant-input")
        summary.send_keys("四级")
        time.sleep(1)
        summary.send_keys(Keys.ENTER)
        neirong = dialog.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/span/span")
        neirong.click()
        time.sleep(1)
        button = dialog.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/button[2]")
        button.click()

        # 向下滚动页面
        self.driver.execute_script('window.scrollBy(0,500)')

        # 输入责任人
        charger_input = self.driver.find_element_by_class_name("antd-pro-pages-field-quality-task-edit-style-selectSuffix")
        #  "/html/body/div/div/section/main/div/form/div[2]/div[1]/div[5]/div[2]/div/span/div/div/div/div[1]")
        charger_input.click()
        time.sleep(1)
        charger_dialog = self.driver.find_element_by_class_name("ant-modal")
        person = charger_dialog.find_element_by_class_name("ant-input")
        person.send_keys("test1")
        time.sleep(2)

        # 定位弹出框中的责任人输入框
        button_submit = charger_dialog.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]")
        #    ("//*[@class='ant-btn ant-btn-primary']") # 这种方式的定位无法使用click/submit，必须使用全写
        time.sleep(1)
        # 选中输入的责任人标签
        select_text = charger_dialog.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/span[1]/span")
        select_text.click()
        time.sleep(2)
        # 选择责任人弹框页面点击提交
        button_submit.click()
        time.sleep(2)

        # 新建问题页面点击提交
        submits = self.driver.find_elements_by_css_selector("#attachment > div.ant-row.ant-form-item.antd-pro-pages-field-common-formtail > div > div > span > button.ant-btn.ant-btn-primary")
        # 滚动页面直至该元素可见（提交按钮）
        submit = submits[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        time.sleep(2)
        submit.click()
        time.sleep(1)


driver_test = DriverTest()
driver_test.open_driver()
driver_test.login()
driver_test.pages()
driver_test.new_question()

# driver_test.quit_driver()




