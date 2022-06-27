# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in list1:
#     if i == 6:
#         continue
# else:
#     print(i)
# print(i)
# for y in range(1,10):
#     x=1
#     while x<=y:
#         z=x*y
#         print(f'{z}={x}x{y}',end=" ")
#         x+=1
#     print('')
# a=[1,2,3,4]
# str1=''
# li1=[]
# for i in a:
#     for j in a:
#         for k in a:
#             if (i!=j) and (j!=k) and (k!=i):
#               li1.append(i*100+j*10+k)
# print(len(li1))
# print(li1)

# sum=0
# for i in range(1,100,2):
#     sum=sum+1/i
# print(sum)
# sum=0
# for i in range(1,100,2):
#     sum=sum+1/i
# print(sum)
# a=1
# i=2
# while i<=10:
#     a=a*i
#     i+=1
# print(a)

# str1='helloppoopo'
# di1={}
# for i in str1:
#     di1[i]=str1.count(i)
# print(di1)
# print(list(range(1,101,2)))
# print(list(range(2,101,2)))
# li1=[1,1,1,2,3,4,4,4,5,6,5,7]
# for i in li1:
#     a=li1.count(i)
#     print(i)
#     if a>1:
#         a=a-1
#         for j in range(a):
#             li1.remove(i)
# print(li1)
# a="k:1|k3:2|k2:9"
# li1=a.split('|')
# di1={}
# for i in li1:
#     li2=i.split(':')
#     di1[li2[0]]=li2[1]
# print(di1)
# str1='user_controller'
# str2=str1.title()
# print(str1.replace('_',''))
# print(str2.replace('_',''))

# list = [2, 6, 9, 10, 18, 15, 1]
# list.sort(reverse=True)
# print(list)
# list.sort(reverse=False)
# print(list)

# list1=[1,1]
# n=20
# for i in range(2,n):
#     list1.append(list1[i-1]+list1[i-2])
# print(list1)
# a =['a','b','c','d','e']
# b =[1,2,3,4,5]
# c={}
# for i in range(len(a)):
#     c[a[i]]=b[i]
# print(c)
#
#
# a = ['apple','banana','apple','tomao','orange','apple','banana','watermeton']
# b={}
# for i in a:
#     b[i]=a.count(i)
# print(b)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []
# b = [i for i in a if i%2==1]
# print(b)

# a='http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_id=203317&trade_type=0'
# li2=a.split('?')[1].split('&')
# di1={}
# for i in li2:
#     c=i.split('=')
#     di1[c[0]]=c[1]
# print(di1)
str1=input('请输入要大写的字符')
str2='asdfghj'
print(str2.replace(str1,str1.upper()))

# for y in range(1,10):
#     x=1
#     while x<=y:
#         z=x*y
#         print(f'{x}x{y}={z}',end=" ")
#         x+=1
#     print('')



