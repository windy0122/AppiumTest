# coding=utf-8
import sys
sys.path.append('../../AppiumTest')
from appium import webdriver
import time
from util.redis_code import RedisCode
from business.register_business import RegisterBusiness
import unittest


class FirstCase(unittest.TestCase):
    def setUp(self):
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

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.register = RegisterBusiness(self.driver)
        self.code_num = RedisCode()
        self.register_phone = '19911111112'

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_register(self):
        self.register.use_base('东方名剪', '吴迪', '123456789', self.register_phone, '123456')
        # self.register.use_owner_info(self.register_phone, '123456')
        self.register.use_code_num(self.code_num.get_code(self.register_phone))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register'))
    unittest.TextTestRunner().run(suite)
