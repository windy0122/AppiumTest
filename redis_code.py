import redis

host_test = '10.12.64.212'
port_test = '6379'

host_uat = '10.12.64.205'
port_uat = '6889'
password_uat = 'v3X7yNFK'

# login_num = '19911111111'



# pool = redis.ConnectionPool(host='10.12.64.212', port='6379', db=4)
# r = redis.StrictRedis(connection_pool=pool)


def get_code(login_num):
    r = redis.Redis(host=host_uat, port=port_uat, db=1, password=password_uat)
    # res = r.get('rts')

    # keys = r.keys()
    # keys = r.get('rts:code_176ab6ba-8ab8-4b55-84cb-99e152d537ad')
    keys = r.keys('rts:code*')
    if keys:
        for key in keys:
            # print(key.decode()[4:])
            values = r.get(key)
            # print(values)
            value = eval(values.decode())
            # print(value)
            # print(type(key))
            # print(res)
    else:
        return None

    # print(type(keys))

    if value['mobile'] == login_num:
        # print(type(value))
        # print(value)
        # code = keys_dec[12:18]
        code = value['smsCode']
        # print(code)
        return code
    else:
        return None

if __name__ == '__main__':
    get_code('19911111111')