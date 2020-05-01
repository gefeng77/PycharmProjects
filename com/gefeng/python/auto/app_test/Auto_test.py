# coding:utf-8
import os
from appium import webdriver

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) # 获取当前项目的根路径

# add some remark message -- need to be deleted

# desired_caps = {}
# desired_caps['platformName'] = 'Android' # 设备系统
# desired_caps['platformVersion'] = '8.0.0' # 设备系统版本
# desired_caps['deviceName'] = '' # 设备名称
# # 测试apk包的路径
# desired_caps['app'] = '/../../XXX.apk'
# # 不需要每次都安装apk
# desired_caps['appPackage'] = 'com.pingan.panj'
# desired_caps['appAitivity'] = 'com.pingan.urbantech.pass.business.foundation.SplashAtivity'
# 如果设置的是app包的路径，则不需要配appPackage和appAcitivy，同理反之

# 自动安装apk到手机
desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "WTKDU16C07004593",
    "app": apk_path + "/phone_test/APP/paas_release_st_ver34234.apk",
    # "appPackage": "com.pingan.panj“,
    # "appAitivity": "com.pingan.urbantech.pass.business.foundation.SplashAtivity",
    # automationName": "Uiautomator2",
    "noReset": "True",
    "unicodeKeyboard": True,
    "resetKeyboard": True
}

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) # 启动app

def always_allow(driver, text, number=5):
    """启动APP时系统弹窗处理
    Args
    - driver -传driver
    - text -需要点击的弹窗文案
    - number -最大点击次数，默认10s
    WebDriver里面0.5s判断一次是否有弹窗，1s超时
    """

    for i in range(number):
        loc = ("xpath", "//*[@text='"+text+"']")
        print(loc)
        try:
            e = WebDriverWait(driver, 1, 0, 5).until(EC.presence_of_element_located)
            e.click()
        except:
            pass


def is_toast_exist(driver, text, timeout=10, poll_frequency=0.5, number=5):
    """is toast exist return True of False
    :param driver: 传driver
    :param text: 页面上看到的文本内容
    :param timeout: 最大超时时间，默认10s
    :param poll_frequency: 间隔查询时间，每隔0.5s查询一次
    :param number:
    :return:
    """
    for i in range(number):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            pass


def swipe_left(driver, t=500, n=1):
    leng = driver.get_window_size()
    x1 = leng['width'] * 0.75
    y1 = leng['height'] * 0.5
    x2 = leng['height'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipe_down(driver, t=500, n=1):
    leng = driver.get_window_size()
    x1 = leng['width'] * 0.5
    y1 = leng['height'] * 0.25
    x2 = len['height'] * 0.5
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipe_up(driver, t=500, n=1):
    leng = driver.get_window_size()
    x1 = leng['width'] * 0.5
    y1 = leng['height'] * 0.75
    x2 = leng['height'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


if __name__ == "__main__":
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    # driver.implicitly_wait(30)
    always_allow(driver, "始终允许")

    # 所有弹窗默认允许
    # for i in range(3):
        driver.switch_to.alert.accept()

    # 点击“允许”按钮
    for i in range(3):
        swipe_left(driver)
        sleep(1)

    # 点击“立即体验”按钮
    # driver.find_element_by_android_uiautomator('new UiSelector().textContains(“立即体验”)').click() # 报错

    driver.find_element_by_id("com.pingan.payj:id/imageView").click()
    sleep(1)

    driver.wait_activity("com.excelliance.kxqp.platform.proxy.gameplugin.ActivityProxy$P00", 10)

    if is_toast_exist(driver, "网络异常"):
        swipe_down(driver)

    # 输入用户名
    driver.find_element_by_class_name("android.widget.EditText")[0].send_keys('15902112282')
    sleep(1)

    # 输入密码
    driver.find_element_by_class_name("android.widget.EditText")[1].send_keys('Aa123456')
    sleep(1)

    # 点击登录按钮
    driver.find_element_by_id("com.pingan.payj:id/btn_login").click()
    sleep(1)

    # 断言登录后的用户名
    # name = driver.find_element_id("com.pingan.payj:id/tv_user_name").text
    # if name == "test1":
    #   print("用户登录成功")
    # else:
    #   print("用户登录失败")

    # 进入“我的”页面
    driver.find_element_by_id("com.pingan.payj:id/iconfont_personal")

    # 点击“退出当前账号”按钮
    driver.find_element_by_id("com.pingan.payj:id/btn_logout").click()
    sleep(1)

    # 点击“退出登录”按钮
    driver.find_element_by_id("button1").click()

    element = driver.find_element_by_id("com.pingan.payj:id/tv_login_title").text
    print(element)
    sleep(1)
    if element == "登录":
        print("用户注销成功")
    else:
        print("用户注销失败")

    driver.quit()