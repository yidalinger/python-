# while True:
#     print('请输入')
#     a=input()
#     if a=='何':
#         print('aa')
#     elif a=='宋':
#         print('bb')
#     elif a=='沈':
#         print('sabi')
#     else:
#         print('啥也不是')
# def fun(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return fun(n-1)+fun(n-2)
# print(fun(20))
# list=[1,1,2]
# for i in range(3,21):
#     list.append(list[i-1]+list[i-2])
# print(list)
# 沈琪洋={}
# 沈琪洋[1]=1
# 沈琪洋[2]=2
# while True:
#     台阶=int(input('请输入台阶数:'))
#     if 台阶<=len(沈琪洋):
#         print(沈琪洋[台阶])
#     else:
#         for i in range(len(沈琪洋)+1,台阶+1):
#             沈琪洋[i]=沈琪洋[i-1]+沈琪洋[i-2]
#         print(沈琪洋[台阶])
# def fun1(x):
#     y=3*x
#     return y
# print(fun1(3))
a=23
print(f'{a:o}')