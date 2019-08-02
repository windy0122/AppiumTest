# coding=utf-8
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


desired_caps = {
    'platformName': 'Android',
    # 1c2033cf 小米8
    # R28M31270TM  三星S10
    'deviceName': '1c2033cf',
    'platformVersion': '9',
    'appPackage': 'com.jiyong.rts',
    'appActivity': 'com.jiyong.login.ui.SplashActivity',
    'automationName': 'Uiautomator2'
}
# time.sleep(5)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


driver.find_element_by_id('com.jiyong.rts:id/tv_sign_in').click()
driver.find_element_by_xpath('//*[@text="账号密码登录"]').click()
# driver.find_element_by_id('com.jiyong.rts:id/ed_register_phone').click()
driver.find_element_by_id('com.jiyong.rts:id/ed_register_phone').send_keys('xxxxxxxxxxxxx')
# driver.find_element_by_id('com.jiyong.rts:id/ed_password').click()
driver.find_element_by_id('com.jiyong.rts:id/ed_password').send_keys('12345')
driver.find_element_by_id('com.jiyong.rts:id/tv_next').click()

# 用于生成xpath定位 相当于 "//*[@text='登录密码错误']"
toast_message = "登录密码错误"
message ="//*[@text=\'{}\']".format(toast_message)

# 获取toast提示框内容
toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
print(toast_element.text)
if toast_element.text == '登录密码错误':
    print('登录失败')


time.sleep(5)

driver.quit()
