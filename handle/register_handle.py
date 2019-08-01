# coding=utf-8
from page.register_page import RegisterPage
import time


class RegisterHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(driver)

    # 点击注册按钮
    def click_start_register(self):
        self.register_p.get_register_start_button().click()

    # 点击保存行业按钮
    def click_save_trade(self):
        self.register_p.get_trade_button().click()

    # 输入店铺名
    def send_shop_name(self, shop_name):
        self.register_p.get_register_shop_name().send_keys(shop_name)

    # 输入店主姓名
    def send_owner_name(self, owner_name):
        self.register_p.get_register_owner_name().send_keys(owner_name)

    # 选择店铺地址
    def choose_shop_address(self):
        self.register_p.get_address_button().click()
        time.sleep(5)
        self.register_p.get_save_address().click()

    # 输入店铺电话
    def send_shop_phone_num(self, phone_num):
        self.register_p.get_shop_phone_num().send_keys(phone_num)

    # 选择营业时间
    def choose_work_time(self):
        self.register_p.get_work_time_button().click()
        time.sleep(3)
        self.register_p.get_save_work_time().click()

    # 点击保存店铺信息
    def save_shop_info(self):
        self.register_p.get_save_shop_info().click()

    # 输入注册手机号
    def send_register_phone_num(self, register_phone_num):
        self.register_p.get_register_phone().send_keys(register_phone_num)

    # 点击获取验证码
    def click_code_button(self):
        self.register_p.get_code_button().click()

    # 输入验证码
    def send_code(self, register_code):
        self.register_p.get_register_code().send_keys(register_code)

    # 输入密码
    def send_password(self, password):
        self.register_p.get_register_password().send_keys(password)

    # 勾选协议
    def choose_clause(self):
        self.register_p.get_clause_check().click()

    # 完成注册
    def click_end_register_button(self):
        self.register_p.get_register_end_button().click()


