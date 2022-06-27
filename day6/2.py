def wfzh(a:'zhanghao'):
    with open("D:\pythonfile\day6\zkh.txt", 'w') as f:
        f.write(' '.join(a))
def rfzh():
    with open('D:\pythonfile\day6\zkh.txt') as f:
       zh =f.read().split(' ')
    return zh
wfzh('aa')

