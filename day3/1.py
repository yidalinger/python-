zh = [['aa', '123456'], ['bb', '123456'], ['cc', '123456']]
grade = {'a': [56, 78, 99],
         'b': [34, 67, 88]}
name = input('请输入账号')
pw = input('请输入密码')
if [name, pw] in zh:
    print('登录成功')
    while True:
        print('查成绩请输入1：\n改或添加成绩请输入2\n退出系统请输入3')
        a = input()
        if a == '1':
            xn = input('请输入学生姓名')
            if xn in grade:
                print(grade[xn])
            else:
                print('学生不存在')
        elif a == '2':
            xn = input('请输入学生姓名')
            a = int(input('亲输入语文成绩'))
            b = int(input('亲输入语文成绩'))
            c = int(input('亲输入语文成绩'))
            grade[xn] = [a, b, c]
        elif a == '3':
            break
        else:
            print('请输入正确的数字')
else:
    print('账号或密码错误')
