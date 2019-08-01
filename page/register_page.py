# coding=utf-8
import sys
sys.path.append('../../AppiumTest')
from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取开始注册按钮元素
    def get_register_start_button(self):
        return self.fd.get_element('register_start_button')

    # 获取行业保存元素
    def get_trade_button(self):
        return self.fd.get_element('trade_button')

    # 获取输入店铺名元素
    def get_register_shop_name(self):
        return self.fd.get_element('register_shop_name')

    # 获取店主姓名元素
    def get_register_owner_name(self):
        return self.fd.get_element('register_owner_name')

    # 获取店铺地址元素
    def get_address_button(self):
        return self.fd.get_element('address_button')

    # 获取保存店铺地址元素
    def get_save_address(self):
        return self.fd.get_element('save_address')

    # 获取预约电话元素
    def get_shop_phone_num(self):
        return self.fd.get_element('shop_phone_num')

    # 获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_element('password_error')

    # 获取营业时间元素
    def get_work_time_button(self):
        return self.fd.get_element('work_time_button')

    # 获取保存营业时间元素
    def get_save_work_time(self):
        return self.fd.get_element('save_work_time')

    # 获取保存店铺信息元素
    def get_save_shop_info(self):
        return self.fd.get_element('save_shop_info')

    # 获取注册手机号元素
    def get_register_phone(self):
        return self.fd.get_element('register_phone')

    # 获取验证码按钮元素
    def get_code_button(self):
        return self.fd.get_element('get_code_button')

    # 获取验证码输入栏元素
    def get_register_code(self):
        return self.fd.get_element('register_code')

    # 获取密码输入栏元素
    def get_register_password(self):
        return self.fd.get_element('register_password')

    # 获取勾选协议元素
    def get_clause_check(self):
        return self.fd.get_element('clause_check')

    # 获取注册完成按钮元素
    def get_register_end_button(self):
        return self.fd.get_element('register_end_button')


