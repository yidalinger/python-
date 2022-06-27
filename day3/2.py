zh= {'aa': '123456', 'bb':'123456', 'cc':'123456'}
name=input('请输入账号')
pw=input('请输入密码')
if name in zh:
    if pw==zh[name]:
        print('登录成功')
    else:
        print('密码错误')
else:
    print('账号错误')