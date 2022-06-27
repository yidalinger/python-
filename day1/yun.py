def addcj(name1,a,b,c):
    list=[name1,a,b,c]
    cj.append(list)
dh=[['aa','123456'],['bb','23456']]
cj=[['aa',23,45,66],['bb',46,88,99],['cc',35,46,34]]
for i in range(0,3):
    name = input('账号：')
    passwd = input('密码：')
    if [name, passwd] in dh:
        print('cg')
        while True:
            na = input('qing12huomingzi:')
            if na == '12':
                name1 = input("名字")
                a = input('数学：')
                b = input('语文：')
                c = input('英语：')
                addcj(name1, a, b, c)
            elif na == 'exit':
                break

            else:
                for i in range(len(cj)):
                    if na == cj[i][0]:
                        print(cj[i])
                        break
                else:
                    print('mei')
        break
    else:
        print(f'失败{i+1}次')



