import redis


class RedisCode(object):
    def __init__(self):
        self.host_test = 'xxxxxx'
        self.port_test = 'xxxxxxxxxx'

        self.host_uat = 'xxxxxxxxxxxx'
        self.port_uat = 'xxxxxxxxxxx'
        self.password_uat = 'xxxxxxxxxxx'

    # login_num = '19911111111'

    # pool = redis.ConnectionPool(host='xxxxxxxxx', port='xxxxxxxx', db=4)
    # r = redis.StrictRedis(connection_pool=pool)

    def get_code(self, login_num):
        r = redis.Redis(host=self.host_uat, port=self.port_uat, db=1, password=self.password_uat)
        # res = r.get('rts')

        # keys = r.keys()
        # keys = r.get('rts:code_176ab6ba-8ab8-4b55-84cb-99e152d537ad')
        keys = r.keys('rts:code*')
        if keys:
            for key in keys:
                values = r.get(key)
                value = eval(values.decode())

            if value['mobile'] == login_num:
                code = value['smsCode']

            else:
                return 'code error'
        else:
            return 'code not in'
        return code

if __name__ == '__main__':
    sms_code = RedisCode()
    print(sms_code.get_code('19911111112'))
