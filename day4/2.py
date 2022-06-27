def login_in(a, b):
    global c
    if a == 'zkh' and b == '123456':
        print('成功')
        c = 1

    else:
        print('失败')
        c = 0


def yuan():
    if c == 1:
        print('1000')
    else:
        print('先输入账号密码')


if __name__ == '__main__':
    name = input('账号:')
    pw = input('密码')
    login_in(name, pw)
    yuan()
