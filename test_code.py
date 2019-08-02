# coding=utf-8
from util.redis_code import RedisCode


sms_code = RedisCode()
code = sms_code.get_code('19911111112')

print(code)
