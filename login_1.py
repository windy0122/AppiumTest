# coding=utf-8
from appium import webdriver
import time
from util.redis_code import get_code


desired_caps = {
    'platformName': 'Android',
    # 1c2033cf 小米8
    # R28M31270TM  三星S10
    # FJH7N18925014194  华为nova3
    'deviceName': 'FJH7N18925014194',
    'platformVersion': '9',
    'appPackage': 'com.jiyong.rts',
    'appActivity': 'com.jiyong.login.ui.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True
    # 'automationName': 'Uiautomator2'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

time.sleep(3)
try:
    driver.find_element_by_id('com.jiyong.rts:id/tv_check_in').click()
    driver.find_element_by_id('com.jiyong.rts:id/tv_next').click()
    # 输入店名
    driver.find_element_by_id('com.jiyong.rts:id/ed_shop_name').send_keys('东方名剪')
    # 输入店主名
    driver.find_element_by_id('com.jiyong.rts:id/ed_owner_name').send_keys('吴迪')
    # 输入电话
    driver.find_element_by_id('com.jiyong.rts:id/ed_booking_phone').send_keys('123456789')
    # 选择营业时间
    driver.find_element_by_xpath('//*[@text="请选择营业时间"]').click()
    driver.find_element_by_id('com.jiyong.rts:id/tv_save').click()
    # 选择地址
    driver.find_element_by_id('com.jiyong.rts:id/tv_address').click()
    time.sleep(5)
    driver.find_element_by_id('com.jiyong.rts:id/txt_right_title').click()

    time.sleep(2)
    driver.find_element_by_id('com.jiyong.rts:id/tv_next').click()

    # 输入手机号
    driver.find_element_by_id('com.jiyong.rts:id/ed_login_name').send_keys('19911111111')
    # 获取验证码，输入验证码
    driver.find_element_by_id('com.jiyong.rts:id/tv_get_verification_code').click()
    time.sleep(2)
    driver.find_element_by_id('com.jiyong.rts:id/ed_check_code').send_keys(get_code('19911111111'))
    driver.find_element_by_id('com.jiyong.rts:id/ed_password').send_keys('123456')
    driver.find_element_by_id('com.jiyong.rts:id/cb_info').click()
    driver.find_element_by_id('com.jiyong.rts:id/tv_next').click()

    time.sleep(5)
    driver.quit()

except:

    time.sleep(5)
    driver.quit()




