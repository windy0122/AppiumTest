# coding=utf-8
import sys
sys.path.append('../../AppiumTest')
from handle.register_handle import RegisterHandle
import time
from util.redis_code import RedisCode


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def use_base(self, shop_name, owner_name, phone_num, register_phone_num, password):
        self.register_h.click_start_register()
        self.register_h.click_save_trade()
        self.register_h.send_shop_name(shop_name)
        self.register_h.send_owner_name(owner_name)
        self.register_h.choose_shop_address()
        self.register_h.send_shop_phone_num(phone_num)
        self.register_h.choose_work_time()
        self.register_h.save_shop_info()

    # def use_owner_info(self, register_phone_num, password):
        self.register_h.send_register_phone_num(register_phone_num)
        self.register_h.click_code_button()
        self.register_h.send_password(password)
        self.register_h.choose_clause()

    def use_code_num(self, code_num):
        self.register_h.send_code(code_num)
        time.sleep(5)
        self.register_h.click_end_register_button()


